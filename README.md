# TimberPunk Backend

FastAPI backend for TimberPunk woodworking e-commerce site.

## Setup

1. **Install PostgreSQL** (if not already installed)
   - macOS: `brew install postgresql`
   - Start: `brew services start postgresql`

2. **Create database**
   ```bash
   createdb timberpunk
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   - Copy `.env.example` to `.env`
   - Update database credentials if needed

5. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

## Default Admin Credentials

- Email: `admin@timberpunk.com`
- Password: `admin123`

**⚠️ Change these in production!**

## API Endpoints

### Public Endpoints
- `GET /products` - List all products (optional `?category=` filter)
- `GET /products/{id}` - Get product details
- `POST /orders` - Create an order (checkout)

### Admin Endpoints (require Bearer token)
- `POST /auth/login` - Admin login (returns JWT token)
- `GET /auth/me` - Get current admin info

- `POST /products` - Create product
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product

- `GET /orders` - List all orders (optional `?status=` filter)
- `GET /orders/{id}` - Get order details
- `PATCH /orders/{id}` - Update order status

## Database Schema

### Products
- id, name, description, short_description, price, category, image_url, options

### Orders
- id, first_name, last_name, email, phone, shipping_address, note, status, total

### OrderItems
- id, order_id, product_id, product_name, product_price, quantity, selected_options, custom_engraving

### Admins
- id, email, hashed_password

## Order Statuses
- `NEW` - Just created
- `IN_PROGRESS` - Being worked on
- `COMPLETED` - Finished
- `CANCELED` - Canceled
