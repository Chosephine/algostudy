
/*
 * 프로그래머스 120894 영어가 싫어요
*/

public class solve035 {
	
	public static long solution(String numbers) {
        long answer = 0;
        int cur_idx = 0;
        while (cur_idx < numbers.length()) {
        	if (numbers.indexOf("zero", cur_idx) == cur_idx) {
        		answer = answer * 10 + 0;
        		cur_idx += 4;
        		continue;
        	} else if (numbers.indexOf("one", cur_idx) == cur_idx) {
        		answer = answer * 10 + 1;
        		cur_idx += 3;
        		continue;
        	} else if (numbers.indexOf("two", cur_idx) == cur_idx) {
        		answer = answer * 10 + 2;
        		cur_idx += 3;
        		continue;
        	} else if (numbers.indexOf("three", cur_idx) == cur_idx) {
        		answer = answer * 10 + 3;
        		cur_idx += 5;
        		continue;
        	} else if (numbers.indexOf("four", cur_idx) == cur_idx) {
        		answer = answer * 10 + 4;
        		cur_idx += 4;
        		continue;
        	} else if (numbers.indexOf("five", cur_idx) == cur_idx) {
        		answer = answer * 10 + 5;
        		cur_idx += 4;
        		continue;
        	} else if (numbers.indexOf("six", cur_idx) == cur_idx) {
        		answer = answer * 10 + 6;
        		cur_idx += 3;
        		continue;
        	} else if (numbers.indexOf("seven", cur_idx) == cur_idx) {
        		answer = answer * 10 + 7;
        		cur_idx += 5;
        		continue;
        	} else if (numbers.indexOf("eight", cur_idx) == cur_idx) {
        		answer = answer * 10 + 8;
        		cur_idx += 5;
        		continue;
        	} else if (numbers.indexOf("nine", cur_idx) == cur_idx) {
        		answer = answer * 10 + 9;
        		cur_idx += 4;
        		continue;
        	}
        }
        return answer;
    }
	
	public static void main(String[] args) {
		String numbers = "onetwothreefourfivesixseveneightnine";
		long answer = solution(numbers);
		System.out.println(answer);
	}
	
	// .replaceAll(); 매소드가 있따..^^
	// Long.parseLong(); 매소드도 있다..^^
}
