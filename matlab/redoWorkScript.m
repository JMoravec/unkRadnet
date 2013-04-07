data = dlmread ('alphaCoefficients');
dateData = data(:,1);
activityData_1 = data(:,3) .* data(:,4);
activityData_2 = data(:,5) .* data(:,6);
totalActivity = activityData_1 + activityData_2;
dateVectors = datevec(num2str(dateData,"%i"),"yyyymmdd");
octaveGoodDates = datenum(dateVectors);
%find the same points after plotting and assign to correctXaxis
%tics('x',correctXaxis,datestr(correctXaxis,2))
