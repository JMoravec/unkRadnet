#include <stdio.h>
#include <string.h>

double timeToHours(int time);

int main( int argc, char *argv[]) {
	int currentChar = 0; //markes current char in file
	char number[256]; 	 //char array holding current processing number
	int numberInt = 0; 	 //int version of currently held number (converted from number array
	int i = 0;
	int j = 0;
	double time = 0;    //initial time (t_stop)
	double timeDiff = 0;   // t - t_stop
	int beta = 0; 		   // beta detections
	double netBeta = 0;	   // beta detections in picoCurries
	int alpha = 0;	       // alpha detections
	double netAlpha = 0;   // alpha detections in picoCurries
	int CFC = 0;  	       // Clean Filter Count
	const double ALPHACALIBRATION = 1.63;
	const double BETACALIBRATION = 1.15;

	//make sure there is only one argument: the filename
	//aka error handeling
	if (argc != 2) {
		printf("Usage: %s dataset\n", argv[0]);
	} else {
		FILE *data = fopen(argv[1], "r");
		FILE *write = fopen(strcat(argv[1], "Activity"),"w");

		if ((data == 0) || (write == 0)) {
			printf("Could not open/find file\n");
			return(1);
		} else {
			//get characters until end of file is reached
			while((currentChar = fgetc(data)) != EOF){
				//ignore lines beginning with '#'
				if(currentChar == '#'){
					while((currentChar = fgetc(data)) != '\n'){
					}
				// get the number up to the ',' and append to char array
				}else if((currentChar != ',') && (currentChar != '\n')) {
					number[i] = currentChar;
					i++;
				//if end of number: reset counter, calculate, and print data to file
				}else if((currentChar == ',') || (currentChar == '\n') || (currentChar == ' ')){
					number[i] = '\0';
					i = 0;
					//copy number into a better sized array
					char numberCopy[strlen(number)+1];
					for(j = 0; j <= (strlen(numberCopy)+1);j++){
						numberCopy[j] = number[j];
					}
					//convert to int
					numberInt = atol(numberCopy,NULL);
					//if no initial time, set it and print beginnings of file
					if (time == 0){
						time = timeToHours(numberInt);
						fprintf(write,"# Date: %s\n# t_stop = %d (HHMMSS)\n",argv[1],numberInt);
						fprintf(write,"# Data is presented as:\n#t-t_stop (hr), Alpha Activity (pCi), t-t_stop (hr), Beta Activity (pCi)\n");
					} else if ((timeDiff == 0) && (CFC == 0) && (alpha == 0) && (beta == 0)){
					//in case time recorded was on new day
						timeDiff = (timeToHours(numberInt)) - time;
						if(timeDiff < 0){timeDiff += 24;}
					} else if ((beta == 0) && (CFC == 0) && (alpha == 0)) {
						beta = numberInt;
					} else if ((CFC == 0) && (alpha == 0)) {
						CFC = numberInt;
					} else if (alpha == 0) {
						alpha = numberInt;
						netBeta = ((double)(beta - CFC - alpha))*BETACALIBRATION;
						netAlpha = (double)alpha * ALPHACALIBRATION;
						//reinitilize variables

						//print to file
						fprintf(write,"%f,%.2f,%f,%.2f\n",timeDiff,netAlpha,timeDiff,netBeta);
						printf("%.2f,%.2f,%.2f\n",timeDiff,netAlpha,netBeta);
						timeDiff = 0;
						beta = 0;
						alpha = 0;
						CFC = 0;
					}
				}
			}
		}
		fclose(data);
		fclose(write);
	}
	return(0);
}

double timeToHours(int x){
	char total[7];
	char hoursHand[3];
	char min[3];
	char sec[3];
	double hours;
	int j = 0;
	int i = 0;
	char check[7];

	sprintf(total,"%d",x);
	if(strlen(total) == 5) {
		strcpy(check,total);
		total[0] = '0';
		for(i = 0; i < strlen(check);i++){
			total[i+1] = check[i];
		}
	}else if (strlen(total) == 4) {
		strcpy(check,total);
		total[0] = '0';
		total[1] = '0';
		for(i = 0; i < strlen(check);i++){
			total[i+2] = check[i];
		}
	}
	for(i = 0; i <=1; i++){
		hoursHand[j] = total[i];
		j++;
	}
	hoursHand[2] = '\0';
	j = 0;

	for(i = 2; i <=3; i++){
		min[j] = total[i];
		j++;
	}
	min[2] = '\0';
	j = 0;

	for(i = 4; i <=5; i++){
		sec[j] = total[i];
		j++;
	}
	sec[2] = '\0';
	j = 0;

	hours = (double)(atoi(hoursHand) + (((double)atoi(min))/60) + (((double)atoi(sec))/3600));
	return(hours);
}
