package src;
import java.util.ArrayList;

/*
 * 프로그래머스 120891 369게임 
*/

public class solve048 {
	public static int solution(int order) {
		ArrayList<Integer> nums = new ArrayList<Integer>();
		int answer = 0;
		
		while (order > 10) {
			nums.add(order%10);
			order /= 10;
		}
		nums.add(order);
		for (int n : nums) {
			if (n == 3 | n == 6 | n == 9) {
				answer += 1;
			}
		}
        
        return answer;
    }
	public static void main(String[] args) {
		int order = 29423;
		int answer = solution(order);
		System.out.println(answer);
	}
}
