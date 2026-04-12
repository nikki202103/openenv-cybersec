tasks = [
    {
        "id": "t1",
        "level": "easy",
        "steps": [
            {"log": "Email from unknown sender asking for password reset", "correct": "flag_alert"},
            {"log": "User clicked suspicious link", "correct": "escalate_case"},
        ]
    },
    {
        "id": "t2",
        "level": "medium",
        "steps": [
            {"log": "Multiple failed login attempts from same IP 192.168.1.5", "correct": "block_ip"},
            {"log": "Account locked due to brute force", "correct": "flag_alert"},
        ]
    },
    {
        "id": "t3",
        "level": "hard",
        "steps": [
            {"log": "Admin login from unknown IP 45.12.33.10", "correct": "flag_alert"},
            {"log": "User gained admin privileges", "correct": "escalate_case"},
            {"log": "Large sensitive data download detected", "correct": "block_ip"},
        ]
    }
]