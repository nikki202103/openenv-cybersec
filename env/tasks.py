tasks = [
    {
        "id": "t1",
        "level": "easy",
        "grader": "env.grader:grade_t1",
        "steps": [
            {"log": "Email from unknown sender asking for password reset", "correct": "flag_alert"},
            {"log": "User clicked suspicious link", "correct": "escalate_case"},
        ]
    },
    {
        "id": "t2",
        "level": "medium",
        "grader": "env.grader:grade_t2",
        "steps": [
            {"log": "Multiple failed login attempts from same IP 192.168.1.5", "correct": "block_ip"},
            {"log": "Account locked due to brute force", "correct": "flag_alert"},
        ]
    },
    {
        "id": "t3",
        "level": "hard",
        "grader": "env.grader:grade_t3",
        "steps": [
            {"log": "Admin login from unknown IP 45.12.33.10", "correct": "flag_alert"},
            {"log": "User gained admin privileges", "correct": "escalate_case"},
            {"log": "Large sensitive data download detected", "correct": "block_ip"},
        ]
    },
    {
        "id": "t4",
        "level": "easy",
        "grader": "env.grader:grade_t4",
        "steps": [
            {"log": "Suspicious macro payload executed in Word document", "correct": "flag_alert"},
            {"log": "Unauthorized access to internal network", "correct": "escalate_case"},
        ]
    },
    {
        "id": "t5",
        "level": "medium",
        "grader": "env.grader:grade_t5",
        "steps": [
            {"log": "Unusual outbound traffic on port 4444", "correct": "scan_log"},
            {"log": "C2 server traffic verified on port 4444", "correct": "block_ip"},
        ]
    },
    {
        "id": "t6",
        "level": "hard",
        "grader": "env.grader:grade_t6",
        "steps": [
            {"log": "Database dumped and transferred to external server", "correct": "flag_alert"},
            {"log": "Ransomware encryption started", "correct": "escalate_case"},
        ]
    }
]