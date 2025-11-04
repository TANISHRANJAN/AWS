# AWS
a serverless web application that does CRUD operation on data through an HTML form hosted on EC2, processes it via Lambda functions, and stores it in DynamoDB.

Architecture Components
EC2 Instance: Hosts a static HTML form API Gateway: REST API endpoint Lambda Functions: Process form data DynamoDB: Stores submitted form data IAM Roles: Secure permissions between services

Detailed Requirements: 

DynamoDB Table Design Create a table named UserSubmissions with: Partition Key: submissionId (String) Attributes: name, email, message, submissionDate, status

Lambda Functions Create two Lambda functions Submission Lambda: Triggered by API Gateway POST request Validates input data Generates unique submissionId Stores data in DynamoDB Returns success/error response Query Lambda: Triggered by API Gateway GET request Retrieves submissions from DynamoDB Supports querying by email or fetching all records

API Gateway REST API with two resources: POST /submit → Submission Lambda GET /submissions → Query Lambda Enable CORS for EC2 domain

EC2 Instance Launch t2.micro instance with Amazon Linux Install web server (Apache/Nginx) Host static HTML form with fields: Name (text, required) Email (email, required) Message (textarea, required) JavaScript to handle form submission to API Gateway

IAM Roles Lambda execution role with DynamoDB read/write permissions EC2 instance profile (if needed) Note: The HTML form should use CSS and Bootstrap.

DYNAMO-DB
<img width="1310" height="557" alt="image" src="https://github.com/user-attachments/assets/298fccd0-3b75-4207-8545-c288e7b8bbba" />

LAMBDA FUNCTIONS:
1.SubmissionLambda:
<img width="1320" height="534" alt="image" src="https://github.com/user-attachments/assets/aaf1e2f6-f26c-470c-97ac-f5479a5e0116" />

2.QueryLambda
<img width="1326" height="563" alt="image" src="https://github.com/user-attachments/assets/763daad9-090c-4a2d-af18-940f7a783b80" />

API GATEWAY:
<img width="1330" height="452" alt="image" src="https://github.com/user-attachments/assets/2c03ca1d-5773-4b6c-a5be-99aefe902d60" />

EC2: 
<img width="1331" height="589" alt="image" src="https://github.com/user-attachments/assets/49412fb9-7b8d-498e-bc58-ce7a5d3e4573" />

IAM:
<img width="1332" height="569" alt="image" src="https://github.com/user-attachments/assets/8bead168-5863-4529-a731-951fdbb2aa13" />

