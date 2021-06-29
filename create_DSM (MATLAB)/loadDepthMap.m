function [depthMap] = loadDepthMap(path)
	fid = fopen(path); 
	[dims, numFrames] = readHeader(fid);
	% 16 bits per cell i.e 4B
	fileData = fread(fid, 'uint16');  
	fclose(fid); 	
	depth = double(fileData);
	depthCountPerMap = prod(dims);
	depthMap = cell(1,numFrames);
	for i=1 : numFrames 
    		currentDepthData = depth(1:depthCountPerMap);
    		depth(1:depthCountPerMap) = [];
    		depthMap{i} = reshape(currentDepthData, dims(1), 			dims(2));    
	end
end  

function [dims,numFrames] = readHeader(fid)
     numFrames = typecast(uint8(fread(fid,2)), 'uint16');
     dims(1) = typecast(uint8(fread(fid,2)), 'uint16');
     dims(2) = typecast(uint8(fread(fid,2)), 'uint16');
end