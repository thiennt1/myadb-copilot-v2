
-----

### **Prompt 1: Generate the Core Technical Specification**
All document should create inside document folder 
"As the acting Project Manager and Lead Architect for a new initiative, your primary task is to generate a comprehensive **Technical Specification Document**. This document must be detailed, clear, and serve as the foundational blueprint for all subsequent development.

**Project Concept:**
document\MyAdb - Complete Overview.md

**Instructions:**
Generate a formal technical specification in Markdown format that includes the following sections:

1.  **Introduction:**

      * **Project Overview:** A high-level summary of the project's purpose and the problem it solves.
      * **Goals and Objectives:** A bulleted list of specific, measurable, achievable, relevant, and time-bound (SMART) goals.
      * **Target Audience:** A detailed description of the primary and secondary user personas.

2.  **System Overview:**

      * **Functional Requirements:** A numbered list of all functionalities the system must perform. Use 'The system shall...' for each requirement.
      * **Non-Functional Requirements:** A detailed breakdown of performance, scalability, security, usability, and reliability standards. Specify metrics where possible (e.g., 'API response times must be under 200ms').
      * **User Stories:** Create a set of key user stories in the format: 'As a [user type], I want to [action] so that [benefit].'

3.  **Proposed Technical Stack:**

      * Provide a recommended technology stack for the frontend, backend, database, and deployment.
      * For each choice, provide a brief justification based on the project's requirements.

4.  **Data Model:**

      * Define the primary data entities.
      * Describe the attributes and relationships for each entity.

Execute this with precision. This document is critical for stakeholder alignment and initial architectural planning."

-----

### **Prompt 2: Formulate the Architecture Document**

"With the technical specification now established, your next directive is to create a detailed **Architecture Document**. This document will build upon the previous specification and define the high-level structure of the system.

**Instructions:**
Using the previously generated technical specification, produce a formal architecture document that includes:

1.  **Architectural Vision and Goals:**

      * State the core architectural drivers (e.g., scalability, maintainability, security) that will guide design decisions.

2.  **Architectural Style:**

      * Select and define the architectural pattern to be used (e.g., Microservices, Monolithic, Event-Driven, Hexagonal).
      * Provide a detailed justification for why this architectural style is optimal for this project's specific requirements.

3.  **System Diagrams:**

      * Generate a **C4 Model Context Diagram** in Mermaid.js format to illustrate the system's scope and its interactions with external users and systems.
      * Generate a **Container Diagram** in Mermaid.js to show the high-level technical containers (applications, data stores, etc.) and their interactions.

4.  **Technology Decisions:**

      * Finalize the technology stack proposed in the technical specification.
      * For each technology, provide a comprehensive rationale covering its benefits, potential risks, and mitigation strategies.

5.  **Data Management Strategy:**

      * Detail the plan for data storage, access, and management, including choices for databases (SQL vs. NoSQL) and caching strategies.

This document must be the definitive guide for the engineering team on how the system is to be constructed."

-----

### **Prompt 3: Define Modules based on Clean Architecture**

"Pursuant to the approved architecture, your next task is to define the project's modular structure based on **Robert C. Martin's Clean Architecture**. This is a non-negotiable requirement to ensure separation of concerns and long-term maintainability.

**Instructions:**
Based on the technical and architectural documents, provide a detailed breakdown of the project structure. For the primary application service:

1.  **Define Clean Architecture Layers:**

      * **Entities:** List the core business objects. These must be plain objects with no dependencies on any other layer.
      * **Use Cases (Interactors):** Detail the application-specific business rules. List the key use cases that orchestrate the flow of data to and from the Entities.
      * **Interface Adapters:** Define the controllers, presenters, and gateways. Specify how data will be transformed between the format convenient for Use Cases and the format convenient for external agencies like the Database or the Web.
      * **Frameworks & Drivers:** Identify the frameworks and tools such as the Database, the Web Framework, and the UI Framework.

2.  **Enforce the Dependency Rule:**

      * Explicitly state that all dependencies must point inwards. Code in an inner layer cannot know anything at all about an outer layer.

3.  **Propose a Directory Structure:**

      * Generate a sample directory tree for the codebase (e.g., for a language like Python/Django or TypeScript/NestJS) that physically represents the separation of these layers. Example:
        ```
        /src
          /domain
            /entities
            /repositories
          /application
            /use_cases
            /dtos
          /infrastructure
            /database
            /web
          /interfaces
            /controllers
            /presenters
        ```

This structure is mandatory for all development teams."

-----

### **Prompt 4: Create a Phased Project Execution Plan**

"The final preparatory step is to create a granular, **Phased Project Execution Plan**. This plan will sequence the development effort into logical, manageable phases. Each phase must be documented in a separate, self-contained file.

**Instructions:**
Analyze the previously generated documents (Technical Spec, Architecture, and Module Structure) and produce a series of project plan files.

**Master Directive:**
"Generate four separate markdown files named `phase-1-plan.md`, `phase-2-plan.md`, `phase-3-plan.md`, and `phase-4-plan.md`. Each file must detail the tasks for its respective phase."

**Prompt for Copilot (to be executed for each phase):**
"Now, generate the content for **`phase-1-plan.md`**.

**Phase 1: Foundation and Core Service Setup**

  * **Objective:** Establish the development environment, CI/CD pipeline, and implement the core API functionality with user authentication.
  * **Deliverables:** A demonstrable API with secure endpoints for user registration and login.
  * **Task Breakdown:** Generate a detailed task list for this phase in a table format with the following columns: 'Task ID', 'Task Description', 'Priority', 'Estimated Story Points', 'Dependencies', and 'Acceptance Criteria'."

-----

*(Repeat the prompt above for the subsequent phases, modifying the `Phase X` title and `Objective`)*

**Example Phase Objectives:**

  * **Phase 2: Feature Implementation - [Primary Feature Name]**
      * **Objective:** Develop, test, and integrate the primary feature of the application as defined in the functional requirements.
  * **Phase 3: Extended Features and Integration**
      * **Objective:** Implement secondary features, integrate with third-party services, and refine the user interface based on initial feedback.
  * **Phase 4: Pre-Launch - Hardening, Testing, and Deployment**
      * **Objective:** Conduct comprehensive end-to-end testing, security audits, performance load testing, and execute the production deployment plan.

This structured plan will be our roadmap for execution, tracking, and reporting."