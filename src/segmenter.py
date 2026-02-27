

# def group_ideaof(segment):
#     clips = []
#     currrent = []
#     dur =0
    
#     for seg in segment:
#         currrent.append(seg)
#         dur += seg['end'] - seg['start']

#         text = seg['text'].strip().lower()

#         its_enough  = dur >= 30
#         idea_end= text.endswith(".") or text.endswith('?') or text.endswith('!')
#         its_to_loong= dur >= 60

#         if  its_enough  and idea_end or its_to_loong:
#             clips.append(currrent)
#             currrent = []
#             dur = 0

#     if currrent:
#         clips.append(currrent)

#     return clips

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model=SentenceTransformer('all-MiniLM-L6-v2')




def ideaof_segment(segments):
    min_duration = 15
    ideal_min = 30
    ideal_max = 35
    max_duration = 60

    pause_threshold = 1.0
    mid_similarity = 0.6
    low_similarity = 0.5

    min_words = 20


    current_segment = []
    current_words = 0
    clips_segment=[]


    for i, seg  in enumerate(segments) :

        current_segment.append(seg)
        # print("current: ",current_segment)
        
        if i == len(segments) - 1:
             break
        
        next_seg = segments[i+1]    

        seg_text = seg['text'].strip().lower()
        next_seg_text= next_seg['text'].strip().lower()
        
        emb1= model.encode(seg_text)
        emb2= model.encode(next_seg_text)

        current_words += len(seg['text'].split())
        duration = current_segment[-1]['end'] - current_segment[0]['start']
        pause = next_seg['start'] - seg['end']

        similarity = cosine_similarity([emb1],[emb2])[0][0]
        print("Similarity: ",similarity)
        boundary = False

        # Strong topic shift
        if similarity < low_similarity:
            boundary = True

        # Pause-based boundary
        elif pause > pause_threshold and similarity < mid_similarity:
            boundary = True

        # Adaptive cut logic
        if boundary:
            if duration >= ideal_min and current_words >= min_words:
                clips_segment.append(current_segment.copy())
                # print("current: ",current_segment)
                current_segment=[]
                current_words=0

        # Hard safety cut
        elif duration >= max_duration:
            clips_segment.append(current_segment.copy())
            print("current: ",current_segment)
            current_segment=[]
            current_words=0
        

    if current_segment:
        clips_segment.append(current_segment.copy())

        # print("Clip: ",clips_segment)

    return clips_segment


def build_segment(segment):
    print("On Segmenter....")
    final_segment=[]
    grouping_segments= ideaof_segment(segment)
    
    for i,seg in enumerate(grouping_segments):
       final_segment.append(format_segment(seg)) 
       print("Count Segment:",i)

    
    # print("Final: ",final_segment)
    return final_segment


def format_segment(segs):
    text=" ".join(s["text"] for s in segs).strip()
    start_time=float(segs[0]["start"])
    end_time=float(segs[-1]["end"])

    return {
        "text":text ,
        "start":start_time ,
        "end":end_time,
        "duration": end_time-start_time
    }



