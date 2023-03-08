import java.util.*;

/*
 * programmers 코딩테스트 입문
 * 개미 군단
*/

public class solve027{
	
	public static int solution(int hp) {
		// 장군 개미는 5의 공격력, 병정개미는 3의 공격력, 개미는 1의 공격력
		int leftHp = hp;
		int answer = 0;
		while (leftHp > 0) {			
			if (leftHp / 5 > 0) {
				answer += leftHp / 5;
				leftHp -= (leftHp / 5) * 5; // 아니 이게 나머지잖아...
			}
			else if (leftHp / 3 > 0) {
				answer += leftHp / 3;
				leftHp -= (leftHp / 3) * 3;// 아니 이것도 나머지잖아...
			} else {
				answer += leftHp;
				leftHp -= leftHp;
			}
		}
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
    	System.out.printf("hello world\n");
//    	int[] inPut = {30, 10, 23, 6, 100};
    	int inPut = 999;
    	int answer = solution(inPut);
//    	ArrayList<Integer> answer = solution(inPut);
    	System.out.println(answer);
    }
}
