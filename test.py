from services import purify_service

o = ["어젠 시발 피자를 먹어", "오늘은 시발 파스타를 먹어"]
for i in o:
    print(purify_service.purify(1, "연인", i))