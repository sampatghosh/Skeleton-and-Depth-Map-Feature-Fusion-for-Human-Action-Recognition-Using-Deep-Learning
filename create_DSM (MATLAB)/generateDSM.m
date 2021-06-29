function generateDSM()
% absolute path of the depth data
loc = 'C:\Users\17033\Desktop\Mtech IT\Minor Project\MHAD Dpth\Pre\Depth\*.mat'
Files=dir(loc);
for k=1:length(Files)	   
	path = fullfile(Files(k).folder,Files(k).name)
	% load the depth data from binary file
	depthMap = loadDepthMap(path);
	% generate dsm
	dsm = DSM(depthMap);
	% show and save the dsm
	showDepthMap(dsm,Files(k).name);
end
end
