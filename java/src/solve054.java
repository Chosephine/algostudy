

import java.util.Arrays;

public class solve054 {
	public static int[] solution(int[] array) {
        int maxElement = 0;
        int maxIndex = 0;
        for (int i=0; i < array.length; i++) {
        	if (array[i] > maxElement) {
        		maxElement = array[i];
        		maxIndex = i;
        	}
        }
        int[] answer = {maxElement, maxIndex};
        
        return answer;
    }
	public static void main(String[] args) {
		int[] inputArray = {1, 8, 3};
		int[] answer = solution(inputArray);
		System.out.println(Arrays.toString(answer));
	}
}
