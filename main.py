from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal, Base
from routers import products, orders, auth_routes
from auth import init_admin
from config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize default admin
db = SessionLocal()
init_admin(db)
db.close()

app = FastAPI(
    title="TimberPunk API",
    description="E-commerce API for TimberPunk woodworking studio",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to TimberPunk API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
