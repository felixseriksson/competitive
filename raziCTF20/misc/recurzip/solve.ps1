# while (True){
	# $name = gci -file *.zip
	# echo $name
	# #& "C:\Program Files\WinRAR\winrar.exe" x emF3cnVmcHluag== *.zip -pzawrufpynj
	# #[Text.Encoding]::Utf8.GetString([Convert]::FromBase64String('TW90w7ZyaGVhZA=='))
# }
for ($i; $i -lt 300; $i++) {
	#rm $oldname
	cd C:\Users\felix\Documents\GitHub\competitive\raziCTF20\misc\recurzip\zipdir
	$file = gci -file *.zip
	$name = $file.Name
	echo $name
	#echo $oldname
	$tmpname = $name.Replace(".zip", "")
	$pwd = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($tmpname))
	$pwd = [string]::Format("-p{0}",$pwd)
	& "C:\Program Files\WinRAR\winrar.exe" x $name *.zip $pwd C:\Users\felix\Documents\GitHub\competitive\raziCTF20\misc\recurzip
	Start-Sleep -Milliseconds 600
	cd ..
	rm zipdir -r
	$newfile = gci -file *.zip
	$newname = $newfile.Name
	mkdir zipdir
	$newdir = [string]::Format("zipdir\{0}",$newname)
	mv $newfile $newdir
	#$oldname = $file.Name
	}