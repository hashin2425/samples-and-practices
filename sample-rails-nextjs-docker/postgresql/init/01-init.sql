-- Create user with password
CREATE USER postgres_user_123456789 WITH PASSWORD 'password_123456789';

-- Grant necessary privileges
ALTER USER postgres_user_123456789 WITH CREATEDB;
ALTER USER postgres_user_123456789 WITH LOGIN;
