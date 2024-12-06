from fastapi import FastAPI, HTTPException
import sqlite3
from models import LoginRequest,RegRequest,Delete,Update,masterRegister

app = FastAPI()
db = "db.db"



app = FastAPI(
    title="UsersDump",                
    description="UserDump Api Made With ❤️", 
    version="1.0.0",       
    swagger_ui_parameters={
        "displayRequestDuration": True,  
        "defaultModelsExpandDepth": -1, 
        "showExtensions": False,        
        "hideTopbar": False,            
    }               
   
)



@app.get("/users")
def get_all_users_info():
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        db_user = cursor.fetchall()
        

       
        users = [{"id": user[0], "first_name": user[1], "last_name": user[2], "username": user[3], "password": user[4]} for user in db_user]
        
        return {"users": users}
    
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@app.post("/master/login")
def login(credentials:masterRegister):
    try:
        conn = sqlite3.connect(db, check_same_thread=False)

        cursor = conn.cursor()

        
        cursor.execute("SELECT id, username, password,key FROM mainusers WHERE username = ?", (credentials.username,))
        user = cursor.fetchone()
        conn.close()

       
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        stored_password = user[2] 
        stored_key = user[3] 

        if credentials.password != stored_password:
            raise HTTPException(status_code=401, detail="Incorrect Password")
        
        if credentials.key != stored_key:
            raise HTTPException(status_code=401, detail="Incorrect Key")
      
        return {"message": "Login successful", "user_id": user[0], "username": user[1],"key":user[3]}

    except:
         raise HTTPException(status_code=505, detail="Invalid User Info")
    


@app.post("/login")
def login(credentials: LoginRequest):
    try:
        conn = sqlite3.connect(db, check_same_thread=False)

        cursor = conn.cursor()

        
        cursor.execute("SELECT id, username, password FROM users WHERE username = ?", (credentials.username,))
        user = cursor.fetchone()
        conn.close()

       
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        stored_password = user[2] 

        if credentials.password != stored_password:
            raise HTTPException(status_code=401, detail="Incorrect password")
        
      
        return {"message": "Login successful", "user_id": user[0], "username": user[1]}

    except:
         raise HTTPException(status_code=505, detail="Invalid User Info")
    

@app.patch("/update")
def update_user(credentials: Update):
    try:
        if not credentials.id:
            raise HTTPException(status_code=400, detail="ID cannot be empty")
        conn = sqlite3.connect(db, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET first_name = ?, last_name = ?, password = ?
            WHERE id = ?
        """, (credentials.first_name, credentials.last_name, credentials.password, credentials.id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"successful": "User has been updated successfully"}    

    except:
        raise HTTPException(status_code=500,detail="Server Error")

@app.delete("/delete")
def DeleteUser(credentials:Delete):
    try:
        if not credentials.id:
            raise HTTPException(status_code=400,detail="Id Empty")
        conn = sqlite3.connect(db, check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?",(credentials.id))
        conn.commit()
        return {"successful":"user has been deleted"}
            

    except:
        raise HTTPException(status_code=500,detail="Server Error")

@app.put("/master/add")
def masterAdd(credentials:masterRegister):
    try:
        if not credentials.username:
            raise HTTPException(status_code=400, detail="Username is required")
        if not credentials.password:
            raise HTTPException(status_code=400, detail="Password is required")
        if not credentials.key:
            raise HTTPException(status_code=400, detail="Key is required")
        
        conn = sqlite3.connect(db, check_same_thread=False)
        cursor = conn.cursor()

        
        cursor.execute("""
            INSERT INTO mainusers (username, password,key) 
            VALUES (?, ?,?)
        """, (credentials.username, credentials.password,credentials.key))

        
        conn.commit()
        conn.close()

        return {"message": "Master registered successfully"}
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Username already exists")
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")



@app.put("/register")
def reg(credentials: RegRequest):
    try:
    
        if not credentials.first_name:
            raise HTTPException(status_code=400, detail="First name is required")
        if not credentials.last_name:
            raise HTTPException(status_code=400, detail="Last name is required")
        if not credentials.username:
            raise HTTPException(status_code=400, detail="Username is required")
        if not credentials.password:
            raise HTTPException(status_code=400, detail="Password is required")
        
        conn = sqlite3.connect(db, check_same_thread=False)
        cursor = conn.cursor()

        
        cursor.execute("""
            INSERT INTO users (first_name, last_name, username, password) 
            VALUES (?, ?, ?, ?)
        """, (credentials.first_name, credentials.last_name, credentials.username, credentials.password))

        
        conn.commit()
        conn.close()

        return {"message": "User registered successfully"}

    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Username already exists")
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")