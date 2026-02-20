
KEYWORDS = ["intinya", "jadi", "kesimpulannya", 
            "yang penting", "tipsnya","jangan",
            "harusnya","biasanya", "tips",
            "pelajaranya","manfaat","ketika",
            "intinya","oke"]

def score_punctuation(word):
    score=0
    # Pertanyaan → sering jadi hook
    score += word.count("?") * 2

    # Ekspresi kuat
    score += word.count("!") * 2

    # Elipsis → jeda dramatis
    score += word.count(".") * 1.5

    # Kalimat pendek (<= 6 kata) → potensi punchline
    words = word.split()
    if 1 < len(words) <= 6:
        score += 1.5

    # Ada koma + potong di tengah kalimat → transisi alami
    if "," in word and len(words) > 6:
        score += 0.5
    
    return score


def score_segments(seg):
       print("On Scorer...")
       text= seg["text"].lower()
       punct_score= score_punctuation(text)
       keyword_score = sum(k in text for k in KEYWORDS)

       length = len(text.split())
       length_score = 1 if 20 <= length <= 120 else -1

       filler_penalty = text.count("eee") + text.count("uh")
    

       return keyword_score + length_score + punct_score - filler_penalty



def pick_top_segments(segments, k=10):
    # print("DEBUG first segment:", segments[0], type(segments[0]))
    for seg in segments:
        seg["score"] = score_segments(seg)

    segments = sorted(segments, key=lambda x: x["score"], reverse=True)
    return segments[:k]
