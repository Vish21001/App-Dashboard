CREATE TABLE apps (
    id BIGINT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50),
    developer_name VARCHAR(150),
    downloads BIGINT DEFAULT 0,
    rating DECIMAL(2,1) DEFAULT 0 CHECK (rating BETWEEN 0 AND 5),
    price DECIMAL(6,2) DEFAULT 0.00 CHECK (price >= 0),
    release_date DATE,
    last_updated DATE,
    is_active BOOLEAN DEFAULT TRUE
);
