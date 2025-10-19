from fastapi import FastAPI, Request
import logging
from app.core.logging_config import setup_logging
from app.api.v1 import auth, products, cart, orders

# -------------------------
# Setup logging first
# -------------------------
setup_logging()
logger = logging.getLogger(__name__)

# -------------------------
# Create FastAPI app with Swagger metadata
# -------------------------
tags_metadata = [
    {"name": "Authentication", "description": "Register, login, logout and manage JWT tokens."},
    {"name": "Products", "description": "Manage products, categories, and search."},
    {"name": "Cart", "description": "Add items, remove items, and view cart."},
    {"name": "Orders", "description": "Place orders, track order status, and payments."},
]

app = FastAPI(
    title="E-Commerce API",
    description="API for an e-commerce platform like Flipkart.",
    version="1.0.0",
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc",     # ReDoc
    openapi_url="/openapi.json",
    openapi_tags=tags_metadata
)

# -------------------------
# Logging middleware
# -------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"➡️ Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"⬅️ Completed request: {request.method} {request.url.path} - Status {response.status_code}")
    return response

# -------------------------
# Include API routers
# -------------------------
app.include_router(auth.router, prefix="/v1/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/v1/products", tags=["Products"])
app.include_router(cart.router, prefix="/v1/cart", tags=["Cart"])
app.include_router(orders.router, prefix="/v1/orders", tags=["Orders"])

# -------------------------
# Simple health check / root
# -------------------------
@app.get("/", summary="Health check endpoint")
def read_root():
    logger.info("Home route accessed.")
    return {"message": "Welcome to E-Commerce API"}
