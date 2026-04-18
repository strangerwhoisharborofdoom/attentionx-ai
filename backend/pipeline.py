from backend.ai_logic import detect_emotional_peaks, generate_hooks, calculate_viral_score

def process_video(video_path):
    peaks = detect_emotional_peaks()
    hooks = generate_hooks()

    results = []

    for i, peak in enumerate(peaks):
        results.append({
            "clip": f"clip_{i}.mp4",
            "hook": hooks[i],
            "score": calculate_viral_score(peak["intensity"])
        })

    return results