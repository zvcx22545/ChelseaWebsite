from flask import Flask, render_template, redirect, url_for ,  request , jsonify , session
from flask_mysqldb import MySQL
import requests
import MySQLdb.cursors
from datetime import datetime
from google.oauth2 import service_account
import googleapiclient.discovery
from PIL import Image
from io import BytesIO
import io
import os
import atexit
import pandas as pd
from werkzeug.utils import secure_filename
from flask_mailman import Mail , EmailMessage
from flask import Flask, Response, send_file,after_this_request,flash
from googleapiclient import discovery



app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


app.config['MAIL_SERVER'] = 'smtp.fastmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'footballcompet@fastmail.com'  # replace with your Gmail email
app.config['MAIL_PASSWORD'] = 'j3cm98sf5aplw5vy'         # replace with your Gmail password


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

credentials = service_account.Credentials.from_service_account_file(
    "E:\MyProject\Chelsea-1\json\mybeer-project-8e1bbcd5496e.json",
    scopes=[ 'https://www.googleapis.com/auth/drive.file']
)

app.config['MYSQL_HOST'] = 'Localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'singha_db'

mysql = MySQL(app)
mail = Mail(app)

@app.route('/')
def started():

    return redirect(url_for('home'))

@app.route('/home')
def home():
    session.pop('user_data', None)
    session.pop('player_data', None)
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register1')
def register1():
    if 'user_data' not in session:
        return redirect(url_for('register'))
    return render_template('register1.html')

@app.route('/register2')
def register2():
    if 'user_data' not in session:
        return redirect(url_for('register'))
    return render_template('register2.html')

@app.route('/register3')
def register3():
    if 'user_data' not in session:
        return redirect(url_for('register'))
    else:
        user_data = session.get('user_data', [])
        playerData = session.get('player_data', [])
        return render_template('register3.html', user_data=user_data,playerData=playerData)

@app.route('/register4')
def register4():
    if 'user_data' not in session:
        return redirect(url_for('register'))
    return render_template('register4.html')

@app.route('/tableresult')
def tableresult():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM arena_db WHERE pending = %s', ('อนุมัติ',))
    approved_arenadata = cursor.fetchall()
    cursor.execute('SELECT * FROM result_db WHERE pending = %s', ('อนุมัติ',))
    approved_resultdata = cursor.fetchall()

    return render_template('TableResult.html', arenadata=approved_arenadata,resultdata=approved_resultdata)


@app.route('/addnameteam' , methods = ['POST'])
def addnameteam():
    msg = ''
    teamData = {
        'stadium' : request.form['stadium-select'],
        'teamName' : request.form['Teamname'],
        'captainName' : request.form['Captain'],
        'phoneCaptain' : request.form['phoneCaptain'],
        'LineID' : request.form['LindID'],
        'email' : request.form['emailCaptian'],
    }
    Teamname = teamData['teamName']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT nameTeam FROM team_db WHERE nameTeam = %s', (Teamname,))
    Teamname_get = cursor.fetchone()
    if Teamname_get:
        msg = 'มีชื่อทีมนี้อยู่แล้ว'
        return render_template('register1.html',msg=msg)
    else:
        if 'user_data' not in session:
            session['user_data'] = [teamData]
            return redirect(url_for('register2'))
        else:
            session['user_data'].append(teamData)
            return redirect(url_for('register2'))
    
@app.route('/addnameplayer' , methods = ['POST'])
def addnameplayer():
    if 'user_data' in session:
            # นำข้อมูลไปใช้งานในที่นี้
        playerData = {
        'nameplayer' : request.form['nameplayer'],
        'dateplayer' : request.form['dateplayer'],
        'phoneCaptain' : request.form['phoneplayer'],
        'nameplayer-2' : request.form['nameplayer-2'],
        'dateplayer-2' : request.form['dateplayer-2'],
        'phoneCaptain-2' : request.form['phoneplayer-2'],
        'nameplayer-3' : request.form['nameplayer-3'],
        'dateplayer-3' : request.form['dateplayer-3'],
        'phoneCaptain-3' : request.form['phoneplayer-3'],
        'nameplayer-4' : request.form['nameplayer-4'],
        'dateplayer-4' : request.form['dateplayer-4'],
        'phoneCaptain-4' : request.form['phoneplayer-4'],
        }
        if 'player_data' not in session:
            session['player_data'] = [playerData]
        else:
            session['player_data'].append(playerData)

    return redirect(url_for('register3'))

@app.route('/upload', methods=['POST'])
def upload():
    user_data_list = session.get('user_data', [])
    teamName = user_data_list[0].get('teamName')

    if teamName:
        # Removed the file check
        filename = secure_filename(request.files['image'].filename)

        # Concatenate 'teamName' with the original filename
        filename_with_teamName = f"{teamName}.jpg"
        
        # Save the original image
        file_path_original = os.path.join(app.config['UPLOAD_FOLDER'], filename_with_teamName)
        request.files['image'].save(file_path_original)

        # Rest of your code...

        return redirect(url_for('register4'))

    return 'Invalid teamName or file not uploaded'

@app.route('/confirm' , methods = ['GET','POST'])
def confirm():
    user_data_list = session.get('user_data', [])
    pending = 'รอดำเนินการ'
    stadium = user_data_list[0].get('stadium')
    teamName = user_data_list[0].get('teamName')
    captainName = user_data_list[0].get('captainName')
    phoneCaptain = user_data_list[0].get('phoneCaptain')
    LineID = user_data_list[0].get('LineID')
    email = user_data_list[0].get('email')
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{teamName}.jpg")
    # Check if the image file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as image_file:
            image_data = image_file.read()
        folder_id = '1n-72wW1QBzvECDGyev8aqNAWxuQdvx33'
        image_link = upload_to_google_drive(image_data, folder_id)
    else:
    # If no image file exists, set image_link to None
        image_link = None

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO team_db VALUES (%s, %s,%s, %s, %s, %s, %s, %s)', (teamName, stadium,captainName,phoneCaptain,email,LineID,image_link, pending,))
    mysql.connection.commit()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT nameTeam from team_db where nameTeam = %s', (teamName,))
    team_id = cursor.fetchone()
    datateam = team_id
    idteam_value = datateam['nameTeam']

    player_data_list = session.get('player_data', [])
    nameplayer = player_data_list[0].get('nameplayer')
    dateplayer = player_data_list[0].get('dateplayer')
    phoneplayer = player_data_list[0].get('phoneCaptain')

    nameplayer2 = player_data_list[0].get('nameplayer-2')
    dateplayer2 = player_data_list[0].get('dateplayer-2')
    phoneplayer2 = player_data_list[0].get('phoneCaptain-2')

    nameplayer3 = player_data_list[0].get('nameplayer-3')
    dateplayer3 = player_data_list[0].get('dateplayer-3')
    phoneplayer3 = player_data_list[0].get('phoneCaptain-3')
    
    nameplayer4 = player_data_list[0].get('nameplayer-4')
    dateplayer4 = player_data_list[0].get('dateplayer-4')
    phoneplayer4 = player_data_list[0].get('phoneCaptain-4')

    # Assuming cursor is your database cursor object
    sql_query = 'INSERT INTO player_db (nameTeam, nameplayer, dateplayer, phoneplayer, nameplayer2, dateplayer2, phoneplayer2, nameplayer3, dateplayer3, phoneplayer3, nameplayer4, dateplayer4, phoneplayer4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s,%s)'
    values = (idteam_value, nameplayer, dateplayer, phoneplayer, nameplayer2, dateplayer2, phoneplayer2, nameplayer3, dateplayer3, phoneplayer3,nameplayer4, dateplayer4, phoneplayer4)

    cursor.execute(sql_query, values)

    mysql.connection.commit()

    return redirect(url_for('home'))



@app.route('/admin' )
def adminhome():

    return render_template('CS-admin.html')


@app.route('/adminlogin' , methods=['GET', 'POST'])
def adminlogin():
    username = request.form.get('username')
    password = request.form.get('password')
    cur = mysql.connection.cursor()
    # Query the database to check if the provided credentials exist
    cur.execute("SELECT * FROM admin WHERE userID = %s AND password = %s", (username, password,))
    admin = cur.fetchone()
    if admin:
        # Successful login
        session['admin_id'] = admin[0]
        return redirect('adminmanagement')
    else:
        # Failed login
        return render_template('CS-admin.html')

@app.route('/adminlogoff' , methods=['GET', 'POST'])
def adminlogoff():
    session.pop('admin_id', None)
    return redirect(url_for('adminhome'))


@app.route('/adminmanagement')
def adminmanagement():
    if 'admin_id' not in session:
        return redirect(url_for('adminhome'))
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT team_db.*, player_db.* FROM team_db INNER JOIN player_db ON team_db.nameTeam = player_db.nameTeam ');
    #fetch on record
    playerData = cursor.fetchall()
    return render_template('teamdetail.html', playerData = playerData)

@app.route('/admincompletion')
def admincompletion():
    if 'admin_id' not in session:
        return redirect(url_for('adminhome'))

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
            'SELECT * FROM arena_db ORDER BY idarena desc')
    #fetch on record
    arenaData = cursor.fetchall()

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
            'SELECT * FROM result_db ORDER BY idresult desc')
    #fetch on record
    resultData = cursor.fetchall()

    return render_template('compete.html' ,arenaData=arenaData,resultData=resultData)

@app.route('/checkpending/<string:team_id>', methods=['POST'])
def checkpending(team_id):
    if request.method == 'POST':
        approve = request.form.get('approve')
        notapprove = request.form.get('not-approve')
        print(notapprove)
        if approve:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE team_db SET pending = "อนุมัติ" WHERE team_db.nameTeam = %s', (team_id,))
            mysql.connection.commit()
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT email from team_db WHERE team_db.nameTeam = %s', (team_id,))
            email = cursor.fetchone()
            sendemail = email
            email_value = sendemail['email']
            msg = EmailMessage(
                "ทางคุณได้อนุมัติเข้าโครงการ SINGHA WORLD OF FOOTBALL SKILLS CHALLENGE",
                ": สวัสดีค่ะ/ครับ ทางคุณได้อนุมัติเข้าร่วมโครงการ SINGHA WORLD OF FOOTBALL SKILLS สามารถติดตามข่าวสารเพิ่มเติมได้ที่ : Facebook : Singha World of Football",
                "footballcompet@fastmail.com",
                [email_value]
            )
            msg.send()

        elif notapprove:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('UPDATE team_db SET pending = "ไม่อนุมัติ" WHERE team_db.nameTeam = %s', (team_id,))
            mysql.connection.commit()
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT email from team_db WHERE team_db.nameTeam = %s', (team_id,))
            email = cursor.fetchone()
            sendemail = email
            email_value = sendemail['email']
            msg = EmailMessage(
                "ขออภัยทางคุณไม่ได้อนุมัติเข้าร่วมโครงการ SINGHA WORLD OF FOOTBALL SKILLS CHALLENGE",
                ": สวัสดีค่ะ/ครับ  ต้องขออภัยทางคุณไม่ได้อนุมัติเข้าร่วมโครงการ SINGHA WORLD OF FOOTBALL SKILLS CHALLENGE สามารถติดตามข่าวสารเพิ่มเติมได้ที่ : Facebook : Singha World of Football",
                "footballcompet@fastmail.com.com",
                [email_value]
            )
            msg.send()

    return redirect(url_for('adminmanagement'))


@app.route('/addcompetition', methods=['POST'])
def add_competition():
    if 'admin_id' not in session:
        return redirect(url_for('adminhome'))
    msg = ''
    competName = request.form.get('competName')
    arenaName = request.form.get('arenaName')

    if arenaName == 'ภาคเหนือ':
        map = 'https://maps.app.goo.gl/4RYhzGwJbsHnMm1j9'
    elif arenaName == 'ภาคตะวันออกเฉียงเหนือ':
        map = 'https://maps.app.goo.gl/R8FVbX5YqsHcyW5H9'
    elif arenaName == 'ภาคใต้':
        map = 'https://maps.app.goo.gl/LJCBBpebK3vF1BJf8'
    elif arenaName == 'ภาคตะวันออก':
        map = 'https://maps.app.goo.gl/xUrED3iWmDcjsx3a7'
    elif arenaName == 'ภาคกลาง':
        map = 'https://maps.app.goo.gl/URWj6dhaWkVr3Hc67'
    else:
        msg ='ไม่พบสนามแข่ง'
    image = request.files['image']
    pending = 'รอการอนุมัติ'
    image_data = image.read()
    # imageresize = resize_image(image_data , max_size=(1000,2000))
    # Additional code to process the data or save information to a database if needed
    # ...
    folder_id = '15hpLG0-jpNJMYh1QCwH0U_0KDFDmrjGp'
    image_link = upload_to_google_drive(image_data, folder_id)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO arena_db VALUES (NULL, %s, %s,%s, %s,%s)', (competName, arenaName,image_link,map,pending,))
    mysql.connection.commit()
    return redirect(url_for('admincompletion',msg=msg))

@app.route('/addresult', methods=['POST'])
def add_result():

    if 'admin_id' not in session:
        return redirect(url_for('adminhome'))
        
    competition_round = request.form['Competition_round'] 
    idarena_data = request.form.get('idarena')
    image = request.files['image']
    image_data = image.read()
    pending = 'รอการอนุมัติ'
    # imageresize = resize_image(image_data , max_size=(1000,2000))
    folder_id = '1Y8dhgPOwuN7kFhH1C91lVdo1LzD-K_Qy'
    image_link = upload_to_google_drive(image_data, folder_id)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT competName FROM arena_db WHERE idarena = %s', (idarena_data,))
    arena = cursor.fetchone()
    compet_name_value = arena['competName']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('INSERT INTO result_db VALUES (NULL, %s, %s, %s, %s, %s)', (idarena_data, compet_name_value, image_link,competition_round,pending, ))
    mysql.connection.commit()
    return redirect(url_for('admincompletion'))

def upload_to_google_drive(image_data, folder_id):
    drive_service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': '1.jpg',
        'mimeType': 'image/jpeg',
        'parents': [folder_id]
    }

    # Use image_data directly in MediaIoBaseUpload
    media = googleapiclient.http.MediaIoBaseUpload(io.BytesIO(image_data), mimetype='image/jpeg')

    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    file_id = file.get('id')
    thumbnail_link = f'https://lh3.googleusercontent.com/d/{file["id"]}'
    return thumbnail_link

@app.route('/confirm_competition/<int:arenaid>', methods=['POST'])
def confirm_competition(arenaid):
    if request.method == 'POST':
        # You can use arenaid directly
        arena_id_value = arenaid
        # ค้นหา URL ของรูปภาพที่อนุมัติ (ให้นำมาจากฐานข้อมูล)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE arena_db SET pending = %s WHERE idarena = %s', ('อนุมัติ', arenaid,))
        mysql.connection.commit()
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM arena_db')
        arenadata = cursor.fetchall()
        return redirect(url_for('admincompletion',arenadata=arenadata))


@app.route('/confirm_rusult/<int:resultid>', methods=['POST'])
def confirm_rusult(resultid):
    if request.method == 'POST':
        # You can use resultid directly
        result_id_value = resultid
        # ค้นหา URL ของรูปภาพที่อนุมัติ (ให้นำมาจากฐานข้อมูล)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE result_db SET pending = %s WHERE idresult = %s', ('อนุมัติ', resultid,))
        mysql.connection.commit()
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM result_db')
        resultdata = cursor.fetchall()
        return redirect(url_for('admincompletion',resultdata=resultdata))

@app.route('/export_to_excel', methods=['POST'])
def export_to_excel():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # Fetch all data from team_db and player_db tables using a JOIN
    query = """SELECT *
           FROM team_db
           JOIN player_db ON team_db.nameTeam = player_db.nameTeam;"""

    cursor.execute(query)
    data = cursor.fetchall()

    # Create a pandas DataFrame from the fetched data
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

    # Set the prefix for the Excel file
    file_prefix = 'team_and_player_data'

    # Set the starting file number
    file_number = 1

    # Folder to store Excel files
    folder_name = 'Excel'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create a unique file name by incrementing the number
    while True:
        file_name = f'{file_prefix}_{file_number}.xlsx'
        file_path = os.path.join(folder_name, file_name)  # Save in the Excel directory

        # Check if the file already exists
        if not os.path.exists(file_path):
            break

        file_number += 1

    try:
        # Create an Excel writer object with XlsxWriter engine
        excel_writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

        # Write the DataFrame to a sheet in the Excel file
        df.to_excel(excel_writer, sheet_name='Data', index=False)

        # Close the Excel writer to save the file
        excel_writer.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error in creating Excel file"

    finally:
        # Close the database cursor
        cursor.close()

    # Return the file for downloading
    return send_file(file_path, as_attachment=True)
    
    
@app.route('/download_stadium_data', methods=['POST'])
def download_stadium_data():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """SELECT competName, arenaName, image, map FROM arena_db;"""
    cursor.execute(query)
    data = cursor.fetchall()

        # Create a pandas DataFrame from the fetched data
   # Create a pandas DataFrame from the fetched data
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

    # Set the prefix for the Excel file
    file_prefix = 'Map_and_Stadium_data'

    # Set the starting file number
    file_number = 1

    # Folder to store Excel files
    folder_name = 'Stadium_table'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create a unique file name by incrementing the number
    while True:
        file_name = f'{file_prefix}_{file_number}.xlsx'
        file_path = os.path.join(folder_name, file_name)  # Save in the Excel directory

        # Check if the file already exists
        if not os.path.exists(file_path):
            break

        file_number += 1

    try:
        # Create an Excel writer object with XlsxWriter engine
        excel_writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

        # Write the DataFrame to a sheet in the Excel file
        df.to_excel(excel_writer, sheet_name='Data', index=False)

        # Close the Excel writer to save the file
        excel_writer.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error in creating Excel file"

    finally:
        # Close the database cursor
        cursor.close()

    # Return the file for downloading
    return send_file(file_path, as_attachment=True)
@app.route('/download_result_data', methods=['POST'])
def download_result_data():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    query = """SELECT arenaName, image, Competition_round FROM result_db;;"""
    cursor.execute(query)
    data = cursor.fetchall()

        # Create a pandas DataFrame from the fetched data
   # Create a pandas DataFrame from the fetched data
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])

    # Set the prefix for the Excel file
    file_prefix = 'Result_and_Stadium_data'

    # Set the starting file number
    file_number = 1

    # Folder to store Excel files
    folder_name = 'result'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Create a unique file name by incrementing the number
    while True:
        file_name = f'{file_prefix}_{file_number}.xlsx'
        file_path = os.path.join(folder_name, file_name)  # Save in the Excel directory

        # Check if the file already exists
        if not os.path.exists(file_path):
            break

        file_number += 1

    try:
        # Create an Excel writer object with XlsxWriter engine
        excel_writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

        # Write the DataFrame to a sheet in the Excel file
        df.to_excel(excel_writer, sheet_name='Data', index=False)

        # Close the Excel writer to save the file
        excel_writer.close()

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error in creating Excel file"

    finally:
        # Close the database cursor
        cursor.close()

    # Return the file for downloading
    return send_file(file_path, as_attachment=True)
    
@app.route('/delete_player/<string:team_id>', methods=['POST'])
def delete_record(team_id):
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # SQL สำหรับลบข้อมูลจากทั้งสองตาราง
        delete_query = """
        DELETE player_db, team_db 
        FROM player_db 
        JOIN team_db ON player_db.nameTeam = team_db.nameTeam 
        WHERE player_db.nameTeam = %s
        """
        cursor.execute(delete_query, (team_id,))
        mysql.connection.commit()
        flash('Record successfully deleted!', 'success')
    except MySQLdb.Error as e:
        flash('Error occurred: {}'.format(e), 'danger')
    except Exception as e:
        flash('An error occurred: {}'.format(e), 'danger')
    return redirect('/adminmanagement')

@app.route('/delete_arena', methods=['POST'])
def delete_arena():
    try:
        arena_id = request.form['arena_id']
        
        # Validate if arena_id is not empty or None
        if arena_id:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM arena_db WHERE idarena = %s', (arena_id,))
            mysql.connection.commit()
            flash('Arena successfully deleted!', 'success')
        else:
            flash('No Arena ID provided', 'warning')

    except MySQLdb.Error as e:
        flash('Error occurred: {}'.format(e), 'danger')
    except Exception as e:
        flash('An error occurred: {}'.format(e), 'danger')
    
    return redirect('/admincompletion')  # Redirect to admin completion page

@app.route('/delete_result', methods=['POST'])
def delete_result():
    try:
        result_id = request.form['result_id']
        
        # Validate if arena_id is not empty or None
        if result_id:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('DELETE FROM result_db WHERE idresult = %s', (result_id,))
            mysql.connection.commit()
            flash('Arena successfully deleted!', 'success')
        else:
            flash('No Arena ID provided', 'warning')

    except MySQLdb.Error as e:
        flash('Error occurred: {}'.format(e), 'danger')
    except Exception as e:
        flash('An error occurred: {}'.format(e), 'danger')
    
    return redirect('/admincompletion')  


if __name__ == '__main__':
    app.run(debug=True)

