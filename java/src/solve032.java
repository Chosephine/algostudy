import java.util.*;
/*
 * programmers 코딩테스트 입문
 * 2차원으로 만들기
*/

public class solve032{

	public static int[][] solution(int[] num_list, int n) {
        int[][] answer = new int[num_list.length / n][n];
        for (int i = 0; i < num_list.length / n; i++) {
//    		System.out.println("=============" + i + "=============" );
        	int[] subArray = new int[n];
        	for (int j = 0; j < n; j++) {
//        		System.out.println(n * i + j);
        		subArray[j] = num_list[n * i + j];
        	}
//        	System.out.println(subArray);
        	answer[i] = subArray;
        }
        return answer;
    }
	
    public static void main(String[] args) throws Exception {
//    	System.out.printf("hello world\n");
    	int[] inPut1 = {100, 95, 2, 4, 5, 6, 18, 33, 948};
    	int inPut2 = 3;
    	int[][] answer = solution(inPut1, inPut2);
    	System.out.println(Arrays.toString(answer));
    	System.out.println(Arrays.deepToString(answer));
    }
}
