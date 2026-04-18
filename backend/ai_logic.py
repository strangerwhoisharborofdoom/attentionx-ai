# Simulated AI logic for AttentionX

def detect_emotional_peaks():
    """
    Simulates detection of high-energy/emotional moments
    """
    return [
        {"start": 5, "end": 15, "intensity": 0.8},
        {"start": 20, "end": 30, "intensity": 0.9},
        {"start": 40, "end": 50, "intensity": 0.85}
    ]


def generate_hooks():
    """
    Simulates LLM-based hook/title generation
    """
    return [
        "This insight will change your mindset",
        "Nobody talks about this",
        "This is powerful advice"
    ]


def calculate_viral_score(intensity):
    """
    Simple viral score formula
    """
    base = 0.7
    return round(base + intensity * 0.3, 2)