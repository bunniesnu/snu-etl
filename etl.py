from util import fetch_data

class ETL:
    def __init__(self, x_csrf_token, legacy_normandy_session):
        self.x_csrf_token = x_csrf_token
        self.legacy_normandy_session = legacy_normandy_session

    def _fetch(self, url):
        return fetch_data(url, self.x_csrf_token, self.legacy_normandy_session)

    def get_dashboard_cards(self):
        url = "https://myetl.snu.ac.kr/api/v1/dashboard/dashboard_cards"
        return self._fetch(url)

    def get_course_announcements(self, course_id, per_page=40, page=1):
        url = (f"https://myetl.snu.ac.kr/api/v1/courses/{course_id}/discussion_topics?only_announcements=true&per_page={per_page}&page={page}&filter_by=all&no_avatar_fallback=1&include[]=sections_user_count&include[]=sections")
        return self._fetch(url)

    def get_course_users(self, course_id, per_page=50):
        url = f"https://myetl.snu.ac.kr/api/v1/courses/{course_id}/users?include_inactive=true&include[]=avatar_url&include[]=enrollments&include[]=email&include[]=observed_users&include[]=can_be_removed&include[]=custom_links&per_page={per_page}"
        return self._fetch(url)
    
    def get_course_board(self, course_id):
        url = f"https://myetl.snu.ac.kr/learningx/api/v1/learningx_board/courses/{course_id}/boards"
        return self._fetch(url)
    
    def get_course_board_posts(self, course_id, board_id, page=1):
        url = f"https://myetl.snu.ac.kr/learningx/api/v1/learningx_board/courses/{course_id}/boards/{board_id}/posts?page={page}&filter=title&keyword="
        return self._fetch(url)
    
    def get_course_board_post(self, course_id, board_id, post_id):
        url = f"https://myetl.snu.ac.kr/learningx/api/v1/learningx_board/courses/{course_id}/boards/{board_id}/posts/{post_id}"
        return self._fetch(url)
    
    def get_assignments(self, course_id, per_page=50):
        url = f"https://myetl.snu.ac.kr/api/v1/courses/{course_id}/assignment_groups?exclude_response_fields[]=description&exclude_response_fields[]=rubric&include[]=assignments&include[]=discussion_topic&override_assignment_dates=true&per_page={per_page}"
        return self._fetch(url)

    def get_assignment_submissions(self, course_id, per_page=50):
        url = f"https://myetl.snu.ac.kr/api/v1/courses/{course_id}/students/submissions?per_page={per_page}"
        return self._fetch(url)