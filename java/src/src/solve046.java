package src;
import java.util.Arrays;

/*
 * 프로그래머스 120889 삼각형의 완성조건 (1)
*/

public class solve046 {
	public static int solution(int[] sides) {
        int answer = 0;
		int longest = 0;
        for (int side : sides) {
        	if (longest < side) {
        		longest = side;
        	}
        }
        
        int sidesSum = Arrays.stream(sides).sum();
        if (sidesSum > 2 * longest) {
        	answer = 1;
        } else answer = 2;
        
        
        return answer;
    }
	public static void main(String[] args) {
		int[] sides = {199, 72, 222};
		int answer = solution(sides);
		System.out.println(answer);
	}
}
