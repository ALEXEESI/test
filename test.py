import SimpleITK as sitk
image = sitk.ReadImage("scan.nrrd")
print(image.GetSize())