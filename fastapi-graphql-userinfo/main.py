from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from graphene import ObjectType, String, Schema, Field
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# Initialize FastAPI app
app = FastAPI()

# Set up database connection
engine = create_engine("postgresql://user:password@localhost/db_name")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))

# Create database tables
Base.metadata.create_all(bind=engine)

# Define SQLAlchemy ObjectType for User model
class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

# Define Query object for GraphQL schema
class Query(ObjectType):
    user = Field(UserObject, id=String())

    def resolve_user(self, info, id):
        db = SessionLocal()
        return db.query(User).filter(User.id == id).first()

# Define GraphQL schema
schema = Schema(query=Query)

# Set up GraphQL endpoint
@app.get("/graphql")
async def graphql_endpoint(query: str, variables: str = None):
    return schema.execute(query, variable_values=json.loads(variables) if variables else None)

# Start FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
