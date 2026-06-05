# TalentStage — AI-Powered Creator & Freelancer Marketplace

TalentStage is an AI-powered freelancer hiring and collaboration platform built for the DevFusion Developers Hackathon 2.0.

The platform connects freelancers and clients in a single ecosystem where creators can showcase portfolios, discover projects, submit proposals, manage contracts, and grow their careers while clients can hire talent efficiently using AI-assisted recommendations.

---

## Problem Statement

Creative and technical freelancers often struggle to showcase their work effectively and connect with suitable clients. Similarly, clients spend significant time searching for qualified professionals and evaluating proposals.

TalentStage solves this problem by combining a portfolio marketplace with AI-powered matching, proposal evaluation, portfolio analysis, and skill verification.

---

## Key Features

### Freelancer Features

* Professional portfolio profiles
* Skills, education, and experience showcase
* Portfolio project gallery
* Proposal submission system
* Active contract management
* Deliverable tracking
* Earnings dashboard
* Client reviews and ratings
* Availability status management

### Client Features

* Project posting and management
* Freelancer discovery
* Proposal review and shortlisting
* Hiring workflow
* Active project tracking
* Milestone approval system
* Freelancer bookmarking
* Ratings and reviews

### Community Features

* Public freelancer feed
* Skill challenges
* Mentorship opportunities
* Knowledge sharing

### User Features

* Single account with multiple roles
* Profile completeness tracking
* Identity verification workflow
* Freelancer and client dashboards

---

## AI Features

### Smart Freelancer Match

Ranks freelancers based on:

* Skill match
* Portfolio quality
* Ratings
* Budget compatibility
* Project relevance

### Proposal Evaluator

Analyzes freelancer proposals and scores them on:

* Relevance
* Clarity
* Quality
* Cost effectiveness

### Portfolio Reviewer

Provides feedback such as:

* Missing project details
* Weak descriptions
* Missing measurable outcomes
* Missing live project links

### Skill Verifier

Generates AI-powered assessments for claimed skills and awards verification badges upon successful completion.

Example:

* Verified React Developer
* Verified Python Developer
* Verified UI/UX Designer

### Project Scoping Assistant

Transforms vague client requirements into:

* Structured project briefs
* Suggested deliverables
* Budget estimates
* Timeline recommendations

---

## Tech Stack

### Frontend

* React
* Vite
* Axios
* CSS

### Backend

* Python
* FastAPI
* AI Integration APIs

### Database

* SQLite / PostgreSQL (depending on deployment)

### AI Services

* Groq API
* Hugging Face Models

---

## Project Structure

```text
TalentStageHackathon/
│
├── Backend/
│   ├── api/
│   ├── ai/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── Frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── context/
│   │   └── assets/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/AvinashReddyMummasani/TalentStageHackathon.git

cd TalentStageHackathon
```

---

## Backend Setup

### Create Virtual Environment

Windows

```bash
cd Backend

python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
cd Backend

python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create:

```text
Backend/.env
```

Example:

```env
HUGGINGFACE_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

### Run Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

Open a new terminal.

```bash
cd Frontend
```

Install dependencies:

```bash
npm install
```

Create:

```text
Frontend/.env
```

Example:

```env
VITE_API_URL=http://127.0.0.1:8000
```

Run development server:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## Environment Variables

### Backend

```env
HUGGINGFACE_API_KEY=
GROQ_API_KEY=
```

### Frontend

```env
VITE_API_URL=
```

---

## Future Enhancements

* Real payment gateway integration
* Resume generation
* AI interview preparation
* AI project estimation
* Real-time messaging
* Video consultation system
* Advanced analytics dashboard
* Recommendation engine improvements

---

## Team

Developed as part of DevFusion Developers Hackathon 2.0.

---

## License

This project is developed for educational and hackathon purposes.
