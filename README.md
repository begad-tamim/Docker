
## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/insurance-prediction-api.git
    cd insurance-prediction-api/medical_cost_model
    ```

2. Create a `.env` file in the `medical_cost_model` directory with the following content:
    ```env
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_DB=your_postgres_db
    PGADMIN_DEFAULT_EMAIL=your_pgadmin_email
    PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
    ```

3. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

### Usage

1. The Flask application will be available at `http://localhost:5000`.
2. The PostgreSQL database will be available at `localhost:5432`.
3. PGAdmin will be available at `http://localhost:8080`.

### API Endpoints

- `GET /`: Returns a welcome message.
- `POST /predict`: Accepts JSON data with an `input` key containing the input features for the prediction. Returns the predicted insurance cost.

### Example Request

```sh
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"input": [value1, value2, ...]}'
