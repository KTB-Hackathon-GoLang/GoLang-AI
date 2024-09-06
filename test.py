import os
import sys
sys.path.append(os.path.abspath('services/'))
import purify_service

print(purify_service.purify("팀장","팀원","미안하다. 너희들을 과대평가해서 미안하다. 너희들로도 이 간단한 프로젝트 정도는 진행할 수 있을 줄 알았다."))