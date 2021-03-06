import os, sys, cgi
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'bin')))
import api_local

config = api_local.get_config()
export_dir = config['local']['export_dir']


if __name__ == '__main__':

    instructor_ids = cgi.FieldStorage().getvalue('id')
    instructors = instructor_ids.split(',')
    enrollments = api_local.read_csv(export_dir + 'enrollments.csv', 'course_id')

    output = []
    
    for instructor in instructors:
        output.append("\nInstructor: %s\n\ncourse_id (canvas_course_id)\tsection_id (canvas_section_id)" % instructor)
        for enrollment in enrollments:
            if enrollment['role'] == "teacher" and enrollment['user_id'] == instructor:
                cid = enrollment['course_id']
                ccid = enrollment['canvas_course_id']
                sid = enrollment['section_id']
                csid = enrollment['canvas_section_id']
                output.append("%s (%s)\t%s (%s)" % (cid,ccid,sid,csid))

    print "Content-type: text/plain\n";
    for line in output:
        print line
