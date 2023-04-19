package src;
import java.util.Arrays;

/*
 * 최댓값 만들기(1) 
*/

// 직접 소팅을 구현해야 할까 고민했지만... sort 메소드 사용 ^.^
// java sort는 퀵소트이다..!

public class solve037 {
	public static int solution(int[] numbers) {
        Arrays.sort(numbers);
        int answer = numbers[numbers.length - 1] * numbers[numbers.length - 2];
        return answer;
    }
	
	public static void main(String[] args) {
		int[] numbers = {0, 31, 24, 10, 1, 9};
		int answer = solution(numbers);
		System.out.println(answer);
	}

}
