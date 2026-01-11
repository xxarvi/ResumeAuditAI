from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Role-specific tips
ROLE_TIPS = {
    "frontend": "Focus on React projects, responsive design, and UI performance.",
    "backend": "Highlight APIs, databases, and scalability work.",
    "data": "Show ML models, datasets, and metrics like accuracy.",
    "devops": "Mention CI/CD pipelines, cloud infra, and automation.",
}


# Skill databases
JOB_SKILLS = {
    "frontend": [
        "javascript",
        "react",
        "html",
        "css",
        "typescript",
        "git",
        "responsive",
        "webpack",
        "redux",
        "jest",
    ],
    "backend": [
        "python",
        "node",
        "java",
        "sql",
        "rest",
        "api",
        "docker",
        "aws",
        "mongodb",
        "postgresql",
    ],
    "fullstack": [
        "javascript",
        "react",
        "node",
        "python",
        "html",
        "css",
        "sql",
        "mongodb",
        "docker",
        "aws",
    ],
    "data": [
        "python",
        "machine learning",
        "sql",
        "pandas",
        "numpy",
        "tensorflow",
        "statistics",
        "analysis",
    ],
    "devops": [
        "docker",
        "kubernetes",
        "aws",
        "linux",
        "ci/cd",
        "terraform",
        "jenkins",
        "git",
    ],
    "product": [
        "product strategy",
        "roadmap",
        "user research",
        "agile",
        "jira",
        "analysis",
        "metrics",
    ],
    "ux": [
        "user research",
        "wireframing",
        "figma",
        "prototyping",
        "design",
        "usability",
        "testing",
    ],
}


def extract_text_from_file(file_path):
    """Extract text from files (simplified version)"""
    try:
        # For demo, just check file extension
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read().lower()
        else:
            # For other files, return a demo text
            return "javascript react html css python sql git docker aws web development software engineer"
    except:
        return "software engineer javascript python developer"


def clean_text(text):
    """Clean the text"""
    text = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def analyze_resume_simple(file_path, role):
    """Simple analysis without external dependencies"""
    resume_text = clean_text(extract_text_from_file(file_path))

    # Get skills for the role
    required_skills = JOB_SKILLS.get(role, JOB_SKILLS["frontend"])

    # Get role tip
    role_tip = ROLE_TIPS.get(role, "")

    # Check which skills are present
    matched_skills = []
    for skill in required_skills:
        if skill in resume_text:
            matched_skills.append(skill)

    missing_skills = [s for s in required_skills if s not in matched_skills]

    # Calculate score
    score = min(100, int((len(matched_skills) / len(required_skills)) * 100))

    # Generate feedback
    feedback = f"""
📝 ACTIONABLE ADVICE:
1. Add missing keywords: {'and '.join(missing_skills[:2]) if missing_skills else 'Focus on quantifiable achievements'}
2. Use bullet points with metrics (e.g., "Improved performance by 40%")
3. Place technical skills in a dedicated "Skills" section
4. Include specific project examples

🎯 ROLE-SPECIFIC TIP:
{role_tip}
"""

    return {
        "ats_score": score,
        "matched_skills": matched_skills[:10],
        "missing_skills": missing_skills[:10],
        "ai_feedback": feedback,
        "role": role,
    }


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify(
        {"status": "healthy", "message": "ResumeAudit AI Backend is running"}
    )


@app.route("/analyze", methods=["POST"])
@cross_origin()
def analyze():
    try:
        print("Received analyze request...")

        if "resume" not in request.files:
            return jsonify({"error": "No resume file provided"}), 400

        file = request.files["resume"]
        role = request.form.get("role", "frontend")

        print(f"Processing file: {file.filename}, Role: {role}")

        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400

        # Save file temporarily
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        print(f"File saved to: {file_path}")

        # Analyze
        result = analyze_resume_simple(file_path, role)
        print(f"Analysis complete. Score: {result['ats_score']}")

        # Clean up
        try:
            os.remove(file_path)
            print("Temporary file removed")
        except:
            pass

        return jsonify(result)

    except Exception as e:
        print(f"Error in analyze: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/test", methods=["GET"])
def test():
    """Test endpoint to verify server is working"""
    return jsonify(
        {
            "message": "Server is working!",
            "endpoints": {
                "GET /health": "Health check",
                "POST /analyze": "Analyze resume",
                "GET /test": "This test endpoint",
            },
        }
    )


if __name__ == "__main__":
    print("🚀 Starting ResumeAudit AI Backend Server...")
    print("📍 Server URL: http://127.0.0.1:5000")
    print("🔗 Endpoints:")
    print("   GET  http://127.0.0.1:5000/health")
    print("   GET  http://0.0.0.0:5000/test")
    print("   POST http://127.0.0.1:5000/analyze")
    print("\n📝 To test from browser:")
    print("   Open: http://127.0.0.1:5000/test")
    print("\n✅ Server is ready to accept connections!")

    app.run(host="0.0.0.0", port=5000, debug=True)
