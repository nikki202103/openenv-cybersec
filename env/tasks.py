tasks = [
    {
        "level": "easy",
        "steps": [
            {"log": "Email from unknown sender asking for password reset", "correct": "flag"},
            {"log": "User clicked suspicious link", "correct": "escalate"},
        ]
    },
    {
        "level": "medium",
        "steps": [
            {"log": "Multiple failed login attempts from same IP 192.168.1.5", "correct": "block_ip"},
            {"log": "Account locked due to brute force", "correct": "flag"},
        ]
    },
    {
        "level": "hard",
        "steps": [
            {"log": "Admin login from unknown IP 45.12.33.10", "correct": "flag"},
            {"log": "User gained admin privileges", "correct": "escalate"},
            {"log": "Large sensitive data download detected", "correct": "block_ip"},
        ]
    }
]