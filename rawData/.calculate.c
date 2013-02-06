/* 
This program will convert the raw data (time,beta,alpha particles) from the dosimitry data book to the full data table for easier processing, less typing by the user, and a way to double check the numbers. 

It is also meant to give full control over the format to be used by the curve fitting program.

You can find the format for the input data in the README file in the rawData folder.

For time and finding the time difference, I changed the numbers to hours and did calculations on the number of hours.

NOTE: technically there IS a limit of 256 digits for each data number, but I assumed that would be big enough to hold any practical data 
*/
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
	//aka simple error handeling
	if (argc != 2) {
		printf("Usage: %s dataset\n", argv[0]);
	} else {
		FILE *data = fopen(argv[1], "r");
		FILE *write = fopen(strcat(argv[1], "Activity"),"w");

		if ((data == 0) || (write == 0)) {
			printf("Could not open/find file\n");
			return(1);
		} else {
			/* 
			This right here is the section to parse the file. As I suck with that stuff, this looks pretty ugly. Basically, it parses the file character by character by using fgetc(). Each time this is called, the next character is pulled from the file. If the chacter is a '#', it will ignore the rest of the line (by pulling more characters until a '\n' is passed, which is why typing the datasheets with Windows won't work).

			When it gets past the commented lines, it will take the first number it sees and sets it to the initial time. 

			Then with each line it calculates the time difference, the net alphaBeta, the net beta, and the corrected alpha and beta numbers, prints these to file as well as to screen. It then repeats until the End Of File is reached.
			*/
			//get characters until end of file is reached
			while((currentChar = fgetc(data)) != EOF){
				if(currentChar == '#'){

				//ignore lines beginning with '#'
					while((currentChar = fgetc(data)) != '\n'){
					}

				}else if((currentChar != ',') && (currentChar != '\n')) {

				// get the number up to the ',' and append to char array
					number[i] = currentChar;
					i++;

				}else if((currentChar == ',') || (currentChar == '\n') || (currentChar == ' ')){

				//if end of number: reset counter, calculate, and print data to file
					number[i] = '\0';
					i = 0;

					//copy number into a better sized array
					char numberCopy[strlen(number)+1];
					for(j = 0; j <= (strlen(numberCopy)+1);j++){
						numberCopy[j] = number[j];
					}

					//convert to int
					numberInt = atol(numberCopy,NULL);

					if (time == 0){

					//if no initial time, set it and print beginnings of file
						time = timeToHours(numberInt);
						fprintf(write,"# Date: %s\n# t_stop = %d (HHMMSS)\n",argv[1],numberInt);

					} else if ((timeDiff == 0) && (CFC == 0) && (alpha == 0) && (beta == 0)){

					//find the time difference between the data time and intial time
						timeDiff = (timeToHours(numberInt)) - time;

						//in case time recorded was on new day
						if(timeDiff < 0){timeDiff += 24;}

					} else if ((beta == 0) && (CFC == 0) && (alpha == 0)) {

						//set the beta number
						beta = numberInt;

					} else if ((CFC == 0) && (alpha == 0)) {

						//set the clean filter count
						CFC = numberInt;

					} else if (alpha == 0) {
					//since this is the last number (if the format is followed correctly), we set the alpha value and calculate the net beta number and net alpha number

						alpha = numberInt;
						netBeta = ((double)(beta - CFC - alpha))*BETACALIBRATION;
						netAlpha = (double)alpha * ALPHACALIBRATION;

						//reinitilize variables, print to file, and print to screen
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
		//close the files
		fclose(data);
		fclose(write);
	}
	return(0);
}

/* 
	This function takes an integer with the format HHMMSS and converts it to the hour number in the day.
*/
double timeToHours(int x){
	char total[7];
	char hoursHand[3];
	char min[3];
	char sec[3];
	double hours;
	int j = 0;
	int i = 0;
	char check[7];

	//change the number to a string to manipulate
	sprintf(total,"%d",x);

	//I have to make sure that the number fits the format correctly
	// This first one adds a zero to the first character if the number wasn't long enough
	// (eg. If the data was taken from anytime from midnight to 10 o'clock
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

	//sepearte the hours,minutes, and seconds (and add a null character to each string)
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

	//Finall convert the strings to numbers and find the total hours
	hours = (double)(atoi(hoursHand) + (((double)atoi(min))/60) + (((double)atoi(sec))/3600));
	return(hours);
}
