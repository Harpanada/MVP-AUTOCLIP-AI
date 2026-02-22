def build_segment(segment):
    final_segment=[]
    grouping_segments= group_ideaof(segment)

    for seg in grouping_segments:
        final_segment.append(format_segment(seg))
    
    return final_segment

def group_ideaof(segment):
    clips = []
    currrent = []
    dur =0
    
    for seg in segment:
        currrent.append(seg)
        dur += seg['end'] - seg['start']

        text = seg['text'].strip().lower()

        its_enough  = dur >= 30
        idea_end= text.endswith(".") or text.endswith('?') or text.endswith('!')
        its_to_loong= dur >= 60

        if  its_enough  and idea_end or its_to_loong:
            clips.append(currrent)
            currrent = []
            dur = 0

    if currrent:
        clips.append(currrent)

    return clips


def format_segment(segs):
    return {
        "start": float(segs[0]["start"]),
        "end": float(segs[-1]["end"]),
        "text": " ".join(s["text"] for s in segs).strip()
    }