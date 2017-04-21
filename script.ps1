$reader = new-object System.IO.StreamReader("C:\xxxxxxxxxxxxxxxxxxxxx")
$count = 1
$fileName = "{0}{1}.{2}" -f ($rootName, $count, $ext)
$upperBound = 10MB
while(($line = $reader.ReadLine()) -ne $null)
{
    Add-Content -path $fileName -value $line
    if((Get-ChildItem -path $fileName).Length -ge $upperBound)
    {
        ++$count
        $fileName = "{0}{1}.{2}" -f ($rootName, $count, $ext)
    }
}

$reader.Close()
