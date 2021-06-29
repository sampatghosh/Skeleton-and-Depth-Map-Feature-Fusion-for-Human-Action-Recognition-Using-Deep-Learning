% crop the image as per ROI
function cropImage()
	% absolute directory location of the source images
    	imageDir = 'C:\Users\17033\Desktop\Mtech IT\Minor Project\MHAD Dpth\DMI border MHAD Final';
    	dinfo = dir( fullfile(imageDir, '*.jpg') );
    	dinfo([dinfo.isdir]) = [];  %remove folders
    	filenames = fullfile(imageDir, {dinfo.name});
    	numfiles = length(filenames);
    	for k = 1 : numfiles
     		sssss = filenames{k};
      	theImage = imread(sssss);
		% values are obtained from the rectangular tracker
      	croppedImage = 	imcrop(theImage,[192.510000000000,51.5100000000000,530.98000	0000000,531.980000000000]);
     		%baseFileName = sprintf(sssss, k);
     		fullFileName = fullfile(imageDir, sssss);
     		imwrite(croppedImage, filenames{k});
    	end
end