import requests

def get_apod_info(apod_date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """
   
    url = 'https://api.nasa.gov/planetary/apod'
    
   
    params = {
        'date': apod_date,
        'thumbs': True  
    }
    
    api_key = 'clqCluxXxmytYpv7rdrtsoy8fWY3n2eGMGhAff8j'
    
    
    response = requests.get(url, params={'api_key': api_key})
    
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch APOD info from NASA API:", response.status_code)
        return None

def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    if 'media_type' in apod_info_dict:
        if apod_info_dict['media_type'] == 'image':
            return apod_info_dict['hdurl'] if 'hdurl' in apod_info_dict else apod_info_dict['url']
        elif apod_info_dict['media_type'] == 'video':
            return apod_info_dict['thumbnail_url']
        else:
            print("Unsupported media type:", apod_info_dict['media_type'])
    else:
        print("No media type information found in APOD info dictionary.")
    return None

def main():
    apod_date = '2024-04-17'
    apod_info = get_apod_info(apod_date)
    if apod_info:
        print("APOD Info:")
        print(apod_info)
        print("APOD Image URL:")
        print(get_apod_image_url(apod_info))
    else:
        print("Failed to fetch APOD info.")

if __name__ == '__main__':
    main()
