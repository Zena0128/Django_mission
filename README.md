# Django_mission 추가한 부분
<br>

### 👾 현재 로그인된 유저와 같은 소속 대학교인 유저들이 작성한 게시글만 보이기

* uri : `/board/sameuniv/`

### 👾 5개 단위 페이지네이션

### 👾 익명으로 게시글/댓글 작성

* **/board/에서 POST 요청** or **/board/{boardId}/comments/에서 POST 요청** or **/board/{boardId}/update/에서 PUT 요청** 시 `isAnonymous`라는 Boolean 변수를 추가로 받음
* `isAnonymous = True`로 request 시, user에 userid가 아닌 "ANONYMOUS"로 들어옴
* /board/sameuniv/에서는 익명 여부와 상관 없이 작성자의 대학교만 같으면 가져와짐
