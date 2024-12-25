import re


def main():
    print(parse(input('HTML: ')))


def parse(s):
    if "iframe" not in s:
        return "None"
    for part in s.split(' '):
        if part.startswith('src'):
            url = part.strip('src=').strip('"></iframe>')
            break
    if html := re.search(r'^https?://(?:www\.)?youtube\.com/embed/(.+)$', url, re.IGNORECASE):
        output = r'https://youtu.be/' + html.group(1)
        return output
    else:
        return 'None'


if __name__ == '__main__':
    main()