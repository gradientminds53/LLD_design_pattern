Mediator
--------
Central coordinator that manages communication between objects.
Example: ChatRoom handles messages between users.

Flyweight
---------
Shares common objects to save memory.
Example: 10,000 trees sharing the same TreeType.

Visitor
-------
Adds new operations without modifying existing classes.
Example: AreaCalculator visiting Circle, Rectangle.

Memento
-------
Saves and restores object state.
Example: Undo/Redo in a text editor.

Iterator
--------
Sequentially access elements without exposing structure.
Example: Python for-loop.

Bridge
------
Separates abstraction from implementation.
Example: RemoteControl works with SonyTV or SamsungTV.

Composite
---------
Treat individual objects and groups uniformly.
Example: File and Folder both support display().

Interpreter
-----------
Defines grammar and evaluates expressions.
Example: SQL parser, mathematical expression evaluator.

MVC
---
Separates Model, View, and Controller responsibilities.
Example: Django, Flask applications.

Dependency Injection
--------------------
Provide dependencies from outside instead of creating them internally.
Example: Inject Database into Service class.


# HLD Interview 80/20

- Load Balancer
- Cache
- Database Scaling
- Queues
- CDN
- Microservices
- API Gateway
- CAP Theorem
- Rate Limiter
- Monitoring


OOP
 ↓
Design Patterns
 ↓
SOLID
 ↓
LLD
 ↓
HLD
    ↓
    Load Balancer
    Cache
    DB Scaling
    Queue
    CDN
    API Gateway
    Microservices
 ↓
System Design
 ↓
Distributed Systems
``

1. Load Balancer
2. Cache
3. Database Scaling
4. Message Queue
5. CDN
6. API Gateway
7. Microservices
8. Event Driven Architecture
9. CAP Theorem
10. Rate Limiter

✅ After these 10, go deeper:

##### Phase 2: Distributed Systems
11. Consistent Hashing
12. Distributed Locking
13. Circuit Breaker
14. Service Discovery
15. Observability

##### If I had to reduce everything to the next 5 must-learn topics after HLD
1. Consistent Hashing
2. CAP Theorem
3. Distributed Locking
4. Saga Pattern
5. CQRS

## SUMMARY 


Think of levels:

L3 (SWE)
    ↓
L4 (SWE II)
    ↓
L5 (Senior)
    ↓
L6 (Staff)
    ↓
L7 (Senior Staff)


A Staff Engineer is expected to design and influence systems across multiple teams.

What L6 Staff Actually Needs
1. Coding & DSA ✅
Algorithms
Data Structures
Problem Solving


Still expected.

2. LLD ✅
SOLID
Design Patterns
Clean Code
Dependency Injection


Expected knowledge.

3. HLD ✅
Load Balancer
Cache
Database
Queue
Microservices


Expected knowledge.

4. Distributed Systems ⭐⭐⭐⭐⭐

Must be very strong.

CAP Theorem
Consistency Models
Distributed Transactions
Saga
CQRS
Event Sourcing
Consensus
Replication
Partitioning

5. System Design ⭐⭐⭐⭐⭐

Design systems like:

Google Drive
YouTube
Gmail
BigQuery
Uber
Netflix


Not just components.

Need tradeoff discussions.

6. Reliability Engineering
SLA
SLO
SLI
Availability
Failover
Disaster Recovery

7. Performance Engineering
Latency
Throughput
Scalability
Backpressure
Bottleneck Analysis

8. Architecture
DDD
Hexagonal Architecture
Clean Architecture
Enterprise Architecture

9. Leadership ⭐⭐⭐⭐⭐

This is where Staff differs from Senior.

A Staff engineer is not just coding.

Expected to:

Lead initiatives

Influence multiple teams

Drive technical vision

Review architecture

Resolve technical conflicts

10. Business Thinking

Example:

Instead of asking:

How do I scale?


Staff asks:

Should I scale?

What is the ROI?

Is complexity justified?

Roadmap to L6 Staff
DSA
    ↓
OOP
    ↓
Design Patterns
    ↓
SOLID
    ↓
LLD
    ↓
HLD
    ↓
Distributed Systems
    ↓
Cloud
    ↓
System Design
    ↓
Architecture
    ↓
Technical Leadership
    ↓
Staff Engineer

If I Had to Compress L6 Preparation into 10 Topics
1. DSA
2. Design Patterns
3. SOLID
4. LLD
5. System Design
6. Distributed Systems
7. Databases
8. Networking Fundamentals
9. Cloud & Kubernetes
10. Technical Leadership

Reality Check

For a Google L6 Staff Engineer, roughly:

Coding / DSA               15%
LLD                        10%
HLD                        20%
Distributed Systems        25%
Architecture               15%
Leadership & Influence     15%


The biggest gap between Senior and Staff is not design patterns. It's:

System Design
Distributed Systems
Technical Leadership
Cross-team Influence


That's the area I'd focus on after finishing your current LLD/HLD journey. 🚀


# REVISIT

Yes ✅

For software design patterns, you've essentially reached the end of the classic journey.

#### GoF (Gang of Four) Design Patterns = 23
Creational (5)
Singleton
Factory Method
Abstract Factory
Builder
Prototype

#### Structural (7)
Adapter
Bridge
Composite
Decorator
Facade
Flyweight
Proxy

#### Behavioral (11)
Strategy
Observer
Command
State
Template Method
Chain of Responsibility
Mediator
Memento
Iterator
Visitor
Interpreter

- What actually matters in interviews?

- Out of 23 patterns, these 10-12 are the most important:

Singleton
Factory
Builder
Strategy
Observer
Decorator
Adapter
Facade
Command
State
Template Method
Chain of Responsibility


- Knowing these thoroughly is usually enough for:

Senior SWE
Staff SWE interviews
LLD interviews
Machine Coding rounds
After Design Patterns

The next subjects are:

SOLID Principles
↓
Dependency Injection
↓
Low Level Design Problems
↓
High Level Design
↓
Distributed Systems
↓
Cloud Architecture

###### Final 10-Second Revision
1. Singleton  -> One

2. Factory    -> Which object?

3. Builder    -> Configure

4. Prototype  -> Copy

5. Strategy   -> Choose algorithm

6. Observer   -> Notify

7. Decorator  -> Add behavior

8. Adapter    -> Translate

9. Facade     -> Simplify

10. Command    -> Action object

11. State      -> State changes behavior

12. Template   -> Fixed workflow

13. Chain      -> Pipeline of handlers

14. Proxy      -> Control access

15. Abstract Factory -> Family of objects


🎯 If you can explain problem → why existing approach fails → how the pattern solves it → one code example, then you're done with Software Design Patterns and can confidently move to SOLID Principles and LLD problems.

