"""FastAPI auto-generated app."""
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="A customer contact manager for my business", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def root():
    return """<h1>A customer contact manager for my business</h1>
    <p>Backend API running. <a href="/docs">API Docs</a></p>
    <p>Admin: <a href="/admin">Admin Panel</a></p>"""

@app.get("/api/health")
def health():
    return {"status": "ok", "app": "A customer contact manager for my business"}

@app.get("/api/contacts")
def list_contacts(db: Session = Depends(get_db)):
    items = db.query(models.Contact).all()
    return [schemas.Contact.model_validate(i) for i in items]

@app.post("/api/contacts")
def create_contact(item: schemas.ContactCreate, db: Session = Depends(get_db)):
    obj = models.Contact(**item.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return schemas.Contact.model_validate(obj)

@app.get("/api/contacts/{item_id}")
def get_contact(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Contact).filter(models.Contact.id == item_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return schemas.Contact.model_validate(obj)

@app.put("/api/contacts/{item_id}")
def update_contact(item_id: int, item: schemas.ContactCreate, db: Session = Depends(get_db)):
    obj = db.query(models.Contact).filter(models.Contact.id == item_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    for k, v in item.model_dump().items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return schemas.Contact.model_validate(obj)

@app.delete("/api/contacts/{item_id}")
def delete_contact(item_id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Contact).filter(models.Contact.id == item_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(obj); db.commit()
    return {"deleted": item_id}


@app.get("/admin", response_class=HTMLResponse)
def admin():
    return """<!DOCTYPE html><html><head><title>Admin</title>
    <script src="https://cdn.tailwindcss.com"></script></head>
    <body class="bg-slate-50 p-8">
    <div class="max-w-4xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">A customer contact manager for my business - Admin</h1>
    <p class="text-slate-600">Open <a class="text-blue-600" href="/docs">API Docs</a> for full CRUD.</p>
    </div></body></html>"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
