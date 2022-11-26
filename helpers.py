# exclude all devices associated with the iso boot locations
				iso_devs = ['/run/archiso/airootfs', '/run/archiso/bootmnt']
				lsblk_info = get_lsblk_info(device_path)
				if any([dev in lsblk_info.mountpoints for dev in iso_devs]):
				if lsblk_info is not None and any([dev in lsblk_info.mountpoints for dev in iso_devs]):
					continue

			information = blkid(f'blkid -p -o export {device_path}')