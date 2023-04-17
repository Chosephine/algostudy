package src;
import java.util.Arrays;

public class solve034 {
	
	public static int[] solution(int[] numbers, String direction) {
		int n = numbers.length;
        int[] answer = new int[n];
        if (direction.equals("right")) {
        	// 0 1 2 => 2 0 1
        	answer[0] = numbers[n-1];
        	for (int i=0; i < n-1; i++) {
        		answer[i + 1] = numbers[i];
        	}
        } else {
        	answer[n-1] = numbers[0];
        	for (int i=0; i < n-1; i++) {
        		answer[i] = numbers[i + 1];
        	}
        }
        return answer;
    }
	
	public static void main(String[] args) {
		int[] numbers = {1, 2, 3};
		String direction = "right";
		int[] answer = solution(numbers, direction);
		System.out.println(Arrays.toString(answer));
	}

}
