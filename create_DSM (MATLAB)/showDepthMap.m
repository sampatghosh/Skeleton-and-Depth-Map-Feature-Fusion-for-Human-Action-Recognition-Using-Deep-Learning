function showDepthMap( depthMap,name )
	imagesc('CData',depthMap);
	set(gca,'YDir','reverse')
	axis([1 size(depthMap,2) 1 size(depthMap,1)]);
	colormap(gray);
	%X = strcat(name(1:end-4),'_',int2str(i));
	saveas(gca,name(1:end-4),'jpeg');
end

