# About Database

## CRUD Operations in Database (MongoDB Example)

CRUD stands for:

- **C** → Create  
- **R** → Read  
- **U** → Update  
- **D** → Delete  

## MongoDB

### What is MongoDB?

MongoDB is a NoSQL, document-oriented database that stores data in flexible, JSON-like documents (called BSON – Binary JSON).

Instead of storing data in rows and columns like traditional relational databases, MongoDB stores data as:

```json
{
  "name": "Ramakrishna",
  "phone": "9876543210",
  "city": "Hyderabad"
}
```

These documents are grouped into collections (similar to tables in SQL databases).

---

### How is MongoDB Different from Other Databases?

The biggest comparison is usually between MongoDB and relational databases like:

- MySQL  
- PostgreSQL  
- Oracle Database  

Let’s compare:

---

1️⃣ Data Structure

| Feature | MongoDB | Relational DB (MySQL, PostgreSQL) |
| --- | --- | --- |
| Data Model | Document (JSON-like) | Tables (rows & columns) |
| Schema | Flexible (dynamic) | Fixed schema |
| Joins | Limited / different approach | Strong JOIN support |

---

2️⃣ Schema Flexibility

MongoDB

- No fixed schema required  
- Each document can have different fields  
- Easy to modify structure  

Relational Database

- Must define schema before inserting data  
- Altering table structure can be complex  

Example:

MongoDB allows:

```json
{ "name": "Ram", "phone": "1234" }
{ "name": "Krishna", "phone": "5678", "city": "Delhi" }
```

In MySQL, both rows must match the same table structure.

---

3️⃣ Scalability

MongoDB

- Designed for horizontal scaling  
- Supports sharding (splitting data across servers)  
- Good for big data & distributed systems  

Traditional SQL Database

- Mostly vertical scaling (increase CPU/RAM)  
- Horizontal scaling is more complex  

---

4️⃣ Performance

MongoDB performs very well for:

- Large volume data  
- High write operations  
- Real-time analytics  
- Rapid development  

Relational databases are better for:

- Complex joins  
- Strong transactional systems (banking, finance)  

---

### Why Choose MongoDB?

Choose MongoDB when:

✅ 1. You need flexible schema
Startup projects where requirements change often.

✅ 2. You are building web/mobile applications
MongoDB works very well with:

- Node.js  
- Flask  
- Django  

✅ 3. You handle JSON data

APIs return JSON → MongoDB stores JSON-like → very natural fit.

✅ 4. Fast prototyping

No need to design complex schemas initially.

✅ 5. Big Data / Microservices

Used in scalable systems and distributed architectures.

---

### When NOT to Choose MongoDB?

Avoid MongoDB if:

❌ You need heavy JOIN operations  
❌ Strong ACID relational constraints are critical  
❌ Complex reporting queries across many related tables  

---

### Simple Summary

| If you want | Choose |
| --- | --- |
| Structured banking system | MySQL / PostgreSQL |
| Flexible web app | MongoDB |
| Complex relational queries | PostgreSQL |
| Rapid development | MongoDB |

---

### Real-World Companies Using MongoDB

Companies using MongoDB include:

- Netflix  
- Uber  
- Adobe  

---

### Final Explanation (In Simple Words)

MongoDB is:

- Flexible  
- Scalable  
- JSON-friendly  
- Easy to use for modern applications  

Traditional SQL databases are:

- Structured  
- Strict  
- Strong for financial and relational systems  

### MongoDB Architecture and Components

What is mongod?

`mongod` is the **MongoDB database server process**.

It is responsible for:

- Accepting client connections
- Managing databases and collections
- Handling read/write operations
- Performing indexing
- Managing storage and memory
- Replication and sharding coordination

When you start MongoDB using:

```bash
mongod
```

You are starting the database server.

---

### Core MongoDB Components

1️⃣ mongod

- Main database server
- Handles data storage and queries
- Runs on default port `27017`

---

2️⃣ mongosh (MongoDB Shell)

- Interactive command-line shell
- Used to interact with MongoDB
- Run queries manually

Example:

```bash
mongosh
```

---

3️⃣ MongoDB Drivers
Drivers allow applications to communicate with MongoDB.

Examples:

- Python Driver → `pymongo`
- Node.js Driver → `mongodb`
- Java Driver → MongoDB Java driver

Applications use drivers to send queries to `mongod`.

---

4️⃣ MongoDB Compass

- GUI tool
- Used to visualize databases
- Useful for beginners

---

5️⃣ WiredTiger Storage Engine

- Default storage engine
- Manages how data is stored on disk
- Provides compression and concurrency control

---

6️⃣ Replica Set

- Provides High Availability
- Multiple `mongod` instances
- One Primary
- Multiple Secondary nodes

---

7️⃣ Sharding

- Horizontal scaling method
- Splits large data across multiple servers
- Used for Big Data applications

---

### MongoDB Architecture Diagram (Simple)

```bash
                    +--------------------+
                    |   Client App       |
                    | (Flask / Node.js)  |
                    +----------+---------+
                               |
                               |
                        MongoDB Driver
                               |
                               v
                    +--------------------+
                    |       mongod      |
                    |  (Primary Server) |
                    +----------+---------+
                               |
                 -----------------------------
                 |                           |
                 v                           v
        +----------------+          +----------------+
        |  Secondary 1   |          |  Secondary 2   |
        |   (Replica)    |          |   (Replica)    |
        +----------------+          +----------------+

Data Stored on Disk using WiredTiger Storage Engine
```

---

### MongoDB Workflow (How It Works)

Step 1: Application Sends Request

Example:
User submits a form in Flask.

Application sends request using driver:

```python
collection.insert_one({"name": "Ram", "city": "Hyderabad"})
```

---

Step 2: Driver Connects to mongod

- Driver connects to MongoDB server at:

```bash
mongodb://localhost:27017
```

- Request is sent to `mongod`

---

Step 3: mongod Processes Request

- Validates request
- Checks indexes
- Applies write operation
- Updates memory cache

---

Step 4: Data Stored in Storage Engine

- WiredTiger stores data on disk
- Data is stored in BSON format
- Compression applied

---

Step 5: Replication (If Replica Set Enabled)

- Primary writes data
- Secondary nodes replicate data
- Ensures high availability

---

Step 6: Response Sent Back

- mongod sends acknowledgment
- Driver returns result to application
- Application shows success message

---

### Internal Working Simplified

```bash
Client Request
     ↓
MongoDB Driver
     ↓
mongod Server
     ↓
Query Planner
     ↓
Storage Engine (WiredTiger)
     ↓
Disk
     ↓
Response Back to Client
```

---

### How MongoDB Stores Data

MongoDB stores:

- Databases
  - Collections
    - Documents (JSON-like BSON)

Example Structure:

```bash
Database: userdb
   |
   +-- Collection: users
           |
           +-- { name: "Ram", phone: "1234" }
           +-- { name: "Krishna", phone: "5678" }
```

---

### Advanced Architecture (Sharded Cluster)

```bash
                +------------------+
                |     Client       |
                +---------+--------+
                          |
                     mongos Router
                          |
        ---------------------------------------
        |                 |                   |
   +-----------+     +-----------+      +-----------+
   | Shard 1   |     | Shard 2   |      | Shard 3   |
   | (mongod)  |     | (mongod)  |      | (mongod)  |
   +-----------+     +-----------+      +-----------+
```

### Components in Sharded Cluster

- mongos → Query router
- Config Servers → Store metadata
- Shards → Store actual data

### High-Level Production Architecture

```bash
                          ┌──────────────────────┐
                          │      End Users       │
                          └──────────┬───────────┘
                                     │
                          ┌──────────▼───────────┐
                          │     Load Balancer    │
                          └──────────┬───────────┘
                                     │
                 ┌───────────────────┼───────────────────┐
                 │                   │                   │
        ┌────────▼────────┐ ┌────────▼────────┐ ┌────────▼────────┐
        │ App Server 1    │ │ App Server 2    │ │ App Server 3    │
        │ (Flask/Node)    │ │ (Flask/Node)    │ │ (Flask/Node)    │
        └────────┬────────┘ └────────┬────────┘ └────────┬────────┘
                 │                   │                   │
                 └───────────────────┼───────────────────┘
                                     │
                             ┌───────▼────────┐
                             │     mongos     │
                             │  Query Router  │
                             └───────┬────────┘
                                     │
           ┌─────────────────────────┼─────────────────────────┐
           │                         │                         │
     ┌─────▼─────┐            ┌──────▼─────┐            ┌─────▼─────┐
     │  Shard 1  │            │  Shard 2   │            │  Shard 3  │
     │ (Replica) │            │ (Replica)  │            │ (Replica) │
     └─────┬─────┘            └──────┬─────┘            └─────┬─────┘
           │                         │                         │
   ┌───────▼───────┐         ┌───────▼───────┐         ┌──────▼────────┐
   │ Primary       │         │ Primary       │         │ Primary       │
   │ Secondary     │         │ Secondary     │         │ Secondary     │
   │ Secondary     │         │ Secondary     │         │ Secondary     │
   └───────────────┘         └───────────────┘         └───────────────┘


                 ┌───────────────────────────────┐
                 │        Config Servers         │
                 │  (Store Cluster Metadata)     │
                 └───────────────────────────────┘
```

### Mongodb shell commands

1️⃣ Start & Connect

| Task | Command |
| ------ | --------- |
| Start MongoDB Server | `mongod` |
| Start MongoDB Shell | `mongosh` |
| Connect to Local MongoDB | `mongosh mongodb://localhost:27017` |
| Connect with Authentication | `mongosh -u username -p password --authenticationDatabase admin` |

---

2️⃣ Database Commands

| Task | Command |
| ------ | --------- |
| Show Databases | `show dbs` |
| Switch / Create Database | `use userdb` |
| Check Current Database | `db` |
| Drop Database | `db.dropDatabase()` |

---

3️⃣ Collection Commands

| Task | Command |
| ------ | --------- |
| Show Collections | `show collections` |
| Create Collection | `db.createCollection("users")` |
| Drop Collection | `db.users.drop()` |

---

4️⃣ CREATE Operations

| Task | Command |
| ------ | --------- |
| Insert One | `db.users.insertOne({ name: "Ram", city: "Hyderabad" })` |
| Insert Many | `db.users.insertMany([{ name: "Ram" }, { name: "Krishna" }])` |

---

5️⃣ READ Operations

| Task | Command |
| ------ | --------- |
| Find All | `db.users.find()` |
| Pretty Output | `db.users.find().pretty()` |
| Find One | `db.users.findOne({ name: "Ram" })` |
| Find with Condition | `db.users.find({ city: "Delhi" })` |
| Limit Results | `db.users.find().limit(2)` |
| Sort Ascending | `db.users.find().sort({ name: 1 })` |
| Sort Descending | `db.users.find().sort({ name: -1 })` |

---

6️⃣ UPDATE Operations

| Task | Command |
| ------ | --------- |
| Update One | `db.users.updateOne({ name: "Ram" }, { $set: { city: "Chennai" } })` |
| Update Many | `db.users.updateMany({ city: "Delhi" }, { $set: { city: "New Delhi" } })` |
| Replace Document | `db.users.replaceOne({ name: "Ram" }, { name: "Ram", city: "Bangalore" })` |

---

7️⃣ DELETE Operations

| Task | Command |
| ------ | --------- |
| Delete One | `db.users.deleteOne({ name: "Ram" })` |
| Delete Many | `db.users.deleteMany({ city: "Mumbai" })` |
| Delete All | `db.users.deleteMany({})` |

---

8️⃣ Query Operators

| Type | Example |
| ------ | --------- |
| Greater Than | `db.users.find({ age: { $gt: 25 } })` |
| Less Than | `db.users.find({ age: { $lt: 40 } })` |
| AND Condition | `db.users.find({ $and: [{ city: "Hyderabad" }, { age: { $gt: 25 } }] })` |
| OR Condition | `db.users.find({ $or: [{ city: "Delhi" }, { city: "Mumbai" }] })` |

---

9️⃣ Index Commands

| Task | Command |
| ------ | --------- |
| Create Index | `db.users.createIndex({ name: 1 })` |
| Show Indexes | `db.users.getIndexes()` |
| Drop Index | `db.users.dropIndex({ name: 1 })` |

---

🔟 User & Admin Commands

| Task | Command |
| ------ | --------- |
| Switch to Admin DB | `use admin` |
| Create User | `db.createUser({ user: "admin", pwd: "password", roles: ["root"] })` |
| Show Users | `db.getUsers()` |

---

1️⃣1️⃣ Replica Set Commands

| Task | Command |
| ------ | --------- |
| Initialize Replica Set | `rs.initiate()` |
| Check Replica Status | `rs.status()` |

---

1️⃣2️⃣ Server Status

| Task | Command |
| ------ | --------- |
| MongoDB Version | `db.version()` |
| Server Status | `db.serverStatus()` |
| Current Connections | `db.serverStatus().connections` |

---

1️⃣3️⃣ Backup & Restore (CLI)

| Task | Command |
| ------ | --------- |
| Backup Database | `mongodump --db userdb --out /backup/` |
| Restore Database | `mongorestore /backup/userdb` |
