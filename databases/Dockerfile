FROM postgres:16-alpine

# Environment variables for PostgreSQL
ENV POSTGRES_USER=sela1234
ENV POSTGRES_PASSWORD=selainbar1234
ENV POSTGRES_DB=postgres
ENV PGDATA=/var/lib/postgresql/data/pgdata

# Create a volume for data persistence
VOLUME ["/var/lib/postgresql/data"]

# Expose the PostgreSQL port
EXPOSE 5432

# Initialize the database with the specified user credentials
USER postgres