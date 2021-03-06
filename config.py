import re
import pytz

PANOPTO_SERVER_NAME = 'huji.cloud.panopto.eu'
PANOPTO_CLIEND_ID = None
PANOPTO_SECRET = None


COURSE_ID = None
SEMESTER = None
YEAR = None
FOLDER_ID = None
GOOGLE_JSON = 'client_secret.json'

YEARS = {2018: '2018-19',
         2019: '2019-20',
         2020: '2020-21',
         2017: '2017-18'}


REGEX = re.compile(r'[\n\r\t]')
ISRAEL = pytz.timezone('Israel')

UCS = """
<Session>
  <Title>Test session with audio, video and a presentation</Title>
  <Description/>
  <Date>2018-01-15T00:00:00.000-00:00</Date>
  <Videos>
    <Video>
      <Start>PT0S</Start>
      <File>primary.mp4</File>
      <Cuts/>
      <TableOfContents>
      </TableOfContents>
      <Type>Primary</Type>
      <Transcripts/>
    </Video>
    <Video>
      <Start>PT0S</Start>
      <File>secondary.mp4</File>
      <Cuts/>
      <TableOfContents/>
      <Type>Secondary</Type>
      <Transcripts/>
    </Video>
  </Videos>
  <Presentations>
  </Presentations>
  <Images/>
  <Cuts>
  </Cuts>
  <Tags/>
  <Extensions/>
  <Attachments/>
</Session>
"""

SIMPLE = """
<Session>
  <Title>{Title}</Title>
  <Description>{Description}</Description>
  <Date>{Date}</Date>
  <Videos>
    <Video>
      <Start>PT0S</Start>
      <File>{Filename}</File>
      <Type>Primary</Type>
    </Video>
  </Videos>
</Session>"""

