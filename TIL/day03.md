# day 3

## git commit message

### To Make Good Commit Messages

__1. 커밋 유형 지정__

+ Feat : 새로운 기능의 추가
+ Fix : 버그 수정
+ Docs : 문서 수정
+ Style : 스타일 관련 기능 (코드 포매팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우), 코드 의미에 영향을 주지 않는 변경사항
+ Refactor : 코드 리팩토링
+ Test : 테스트 코드, 리팩토링 테스트 코드 추가
+ Chore : 빌드 업무 수정, 패키지 매니저 수정

__2. 제목과 본문을 빈 행으로 분리__

+ git commit editor를 사용해 여러 행으로 구분된 커밋 메세지를 사용한다

+ 커밋 메세지 템플릿을 작성한 이후(나의 경우는 .gitmessage.txt 로 작성)

  `git config --global commit.template <.gitmessage.txt 경로>`

  다음과 같은 코드를 사용해 추가한다.

+ 탬플릿의 내용은 자유롭지만 나는 이렇게 사용할 것이다.  출처 : https://chanhuiseok.github.io/posts/git-4/

```
# <타입> : <제목> 형식으로 작성하며 제목은 최대 50글자 정도로만 입력
# 제목을 아랫줄에 작성, 제목 끝에 마침표 금지, 무엇을 했는지 명확하게 작성

################
# 본문(추가 설명)을 아랫줄에 작성

################
# 꼬릿말(footer)을 아랫줄에 작성 (관련된 이슈 번호 등 추가)

################
# feature : 새로운 기능 추가
# fix : 버그 수정
# docs : 문서 수정
# test : 테스트 코드 추가
# refactor : 코드 리팩토링
# style : 코드 의미에 영향을 주지 않는 변경사항
# chore : 빌드 부분 혹은 패키지 매니저 수정사항
################
```

+ 커밋을 할 경우에는 다음 명령어를 사용한다

  `git commit`

  commit만 사용하면 vim에 진입하게된다. vim에서는 앞서 작성한 메세지 템플릿이 나타난다.

+ 커밋 메세지를 모두 작성한 이후에는  vim에서 나간다

  esc를 누르고 다음 명령어를 사용한다.

  `:wq`

+ 만약 esc로 메세지 편집에서 빠져나온 경우에 다시 메세지를 작성하려면 'i'를 누른다.

__3. 제목 행을 50자로 제한__

+ 강제는 아니고 간결한 표현을 위해서 지키도록 한다

__4. 제목 행의 첫 글자는 대문자로__

__5. 제목 행 끝에는 마침표를 넣지 않는다__

__6. 제목 행에 명령문을 사용한다.__

+ 명령이나 설명하듯이 간결하게 작성

__7. 본문은 72자마다 끊어서 작성한다__

__8. 본문을 사용하여 변경한 내용과 이유를 설명한다__

+ 어떻게 보다는 무엇을 왜 변경하였는지 설명한다.

__9. 검토자가 아무것도 모른다고 생각하고 자세하게 설명한다__

__10. 자신의 코드가 직관적으로 파악할 수 있다고 생각하지 말자__

__11. 팀에서 정한 commit 규칙을 따르자__



## git reset

+ 커밋 로그를 보기 위한 명령어

  `git log --oneline`

커밋을 했던 로그를 다시 되돌리고 싶을 때 git reset을 사용한다

1. 커밋 로그를 확인하여 돌아가고싶은 커밋 아이디를 확인한다.
2. git reset을 사용한다.

git reset은 --soft, --mixed, --hard 의 3가지 기능이있다.

```
git reset --soft [commit id]
git reset --mixed [commit id]
git reset --hard [commit id]
```

1. soft

   + --soft 를 사용하면 commit만 되돌리는 것이다.

     워킹 디렉토리와 스테이징 에어리어에 내용은 reset을 사용하기 전과 동일하다.

     + ex) git reset soft [ver.4 id]  ==>   w.d -> ver.5   s.a -> ver.5 /// commit -> ver.4

2. mixed
   + --mixed 를 사용하면 commit과 s.a까지 되돌린다.
     + ex) git reset soft [ver.4 id]  ==>   w.d -> ver.5  ///  s.a -> ver.4 commit -> ver.4

3. hard
   + --hard 를 사용하면 전부 되돌린다.
     + ex) git reset soft [ver.4 id]  ==>   w.d -> ver.4  s.a -> ver.4  commit -> ver.4

+ git reset 을 사용한 이후에는 *절대*  push하지 않는다.

  다른 사람들도 코드를 공유할 수 있기 때문에 다른 로컬 저장소와 원격 저장소와의 차이가 발생할 수 있기 때문이다.



## git revert

### git reflog

+ 삭제된 git 로그를 볼 수 있는 명령어

  `git reflog`

  해당 명령어를 사용하면 삭제된 깃 로그를 모두 확인할 수 있다.

+ git reflog를 사용하여 확인한 git id를 사용해 원래대로 커밋을 되돌릴 수 있다.
  1. `git reflow` 명령어로 삭제된 commit id 확인 후
  2. `git reset --hard [commit id]` 



### git revert

+ 취소하고 싶은 커밋을 지웠다는 커밋을 추가하는 명령어.

  `git revert [취소하고싶은 commit id]`

+ reset과의 차이점.

  1. reset은 commit 자체를 삭제하지만 revert는 commit은 남아있고 해당 commit을 취소했다는 로그를 남기는 것.

  2. a, b, c 3개의 commit이 있는 상태에서 `git reset a` 를 하게되면 `git log --oneline` 으로 확인했을 때 남아있는 commit은 b, c

  3. a, b, c 3개의 commit이 있는 상태에서 `git revert a` 를 하게되면 `git log --oneline` 으로 확인했을 때 남아있는 commit은 a, b, c, revert b
  4. 여기서 남아있는 commit 중에서 revert b는 b라는 commit을 지웠다는 내용
  5. reset을 통해서 commit을 삭제하면 github에 push했을때 혼동이 생기지만 revert는 새로운 commit을 추가하면서 특정 commit을 지우는 것이기 때문에 혼동이 생기지 않음
  6. 즉, 특정 commit을 지웠다고 선언하는 것.



## branch

branch는 git 을 사용하면서 master에 코드를 새로운 갈래로 만들어서 사용하는 것이다. master에서 branch가 나오면 branch에서 어떤 테스트를 실행하더라도 master에는 영향을 주지 않는다. `git log --oneline` 으로 확인했을 때 head가 가리키는 곳이 현재 작업중인 branch이다.

+ branch를 조회하는 명령어

  `git branch`

+ branch를 만드는 명령어

  `git branch hotfix`

+ 작업 중인 branch를 이동

  `git switch [branch name]`

  작업 중인 branch를 이동하면 git graph에 나오는 커밋으로 이동하게된다.

+ 
